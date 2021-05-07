import flask
from flask import request, jsonify
from propre_tree import make_tree
from propre_verfiy import verify
from propre_mail import make_email
import re
from flask_cors import CORS

def check(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
        return False

def add_header(data):
    data = jsonify(data)
    data.headers.add("Access-Control-Allow-Origin", "*")
    return data

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/propre-api/proof', methods=['GET', 'POST'])
def api_propre_proof():

    # files = []

    # if 'files' in request.args:
    #     files = request.args['files'].split()
    # else:
    #     error = {"Error" : "No Files Provided."}
    #     return add_header(error)

    # hashes = []
    # if 'hashes' in request.args:
    #     hashes = request.args['hashes'].split()
    # else:
    #     error = {"Error" : "No Hashes Provided."}
    #     return add_header(error)

    # if len(files)!=len(hashes):
    #     error = {"Error" : "Different Number of Files and Hashes."}
    #     return add_header(error)

    # if len(files)==0:
    #     error = {"Error" : "No Files Sent."}
    #     return add_header(error)

    # email = ''
    # if 'email' in request.args:
    #     email = request.args['email']

    # results = make_tree(files, hashes)

    # if email!='' and check(email):
    #     make_email(email, results)

    # results = add_header(results)
    # # results = jsonify(results)
    # # results.headers.add("Access-Control-Allow-Origin", "*")

    # return results

    data = request.get_json(force=True)
    # print(data)
    files = []
    hashes = []

    try:
        for file_name in data["Files"]:
            files.append(file_name)
            hashes.append(data["Files"][file_name])
    except:
        error = {"Error" : "JSON Error"}
        return add_header(error)
    
    if len(files)!=len(hashes):
        error = {"Error" : "Different Number of Files and Hashes."}
        return add_header(error)

    if len(files)==0:
        error = {"Error" : "No Files Sent."}
        return add_header(error)

    email = ''
    try:
        email = data["Email ID"]
    except:
        pass

    results = make_tree(files, hashes)
    # print(results)
    if email!='' and check(email):
        make_email(email, results)

    results = add_header(results)
    # results = jsonify(results)
    # results.headers.add("Access-Control-Allow-Origin", "*")

    return results

@app.route('/propre-api/verify', methods=['GET', 'POST'])
def api_propre_verify():

    transaction_id = ''

    if 'txid' in request.args:
        transaction_id = request.args['txid']
    else:
        error = {"Error" : "No Transaction ID Provided."}
        return add_header(error)

    file_hash = ''
    if 'hash' in request.args:
        file_hash = request.args['hash']
    else:
        error = {"Error" : "No Hash Provided."}
        return add_header(error)

    path_hash = ''
    if 'path' in request.args:
        path_hash = request.args['path']
    else:
        error = {"Error" : "No Path Provided."}
        return add_header(error)

    results = verify(transaction_id, file_hash, path_hash)

    results = {"verify" : results}

    results = add_header(results)

    return results

if __name__ == '__main__':
    app.run(threaded=True)
