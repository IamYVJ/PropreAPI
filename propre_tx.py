import requests
import json
from dotenv import load_dotenv
from os import environ

def make_transaction(data):
    url = "https://api.cryptoapis.io/v1/bc/btc/testnet/txs/new"

    load_dotenv(dotenv_path='.env')

    API_KEY = environ.get("API_KEY")
    ADDRESS = environ.get("ADDRESS")
    WIFS = environ.get("WIFS")

    tx_amount = 0.00000001
    fee = 0.00000249

    payload = json.dumps({
    "createTx": {
        "inputs": [
        {
            "address": ADDRESS,
            "value": tx_amount
        }
        ],
        "outputs": [
        {
            "address": ADDRESS,
            "value": tx_amount
        }
        ],
        "fee": {
        "address": ADDRESS,
        "value": fee
        },
        "data": data,
        "replaceable": False
    },
    "wifs": [
        WIFS
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'X-API-Key': API_KEY
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code==200:
        response_data = response.json()["payload"]
        response_data["blockchain"] = 'https://www.blockchain.com/btc-testnet/tx/' + response_data["txid"]
        del response_data["view_in_explorer"]
        return response_data
    elif response.status_code==400:
        return response.json()["meta"]
    else:
        return {"Error" : response.text}

def get_transaction(tx_id):

    url = "https://api.blockcypher.com/v1/btc/test3/txs/" + tx_id

    response = requests.request("GET", url)

    if response.status_code==200:
        response_data = response.json()
        for output in response_data["outputs"]:
            if output["script_type"]=='null-data':
                return output
    elif response.status_code==404:
        return {"Error" : response.json()["error"]}
    
    return {"Error" : response.text}

# data = "F))))))))))))))))))))))))))))))))))))))))))"
# print(make_transaction(data))

# tx_id = "5ed9f4571b8eef9b4925e7fc638acdfdd548ffeda488baee0864dfb2e06d1626"
# print(get_transaction(tx_id))