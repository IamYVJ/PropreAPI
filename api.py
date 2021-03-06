import flask
from flask import request, jsonify, render_template
from propre_tree import make_tree
from propre_verfiy import verify
# from propre_mail import make_email
from propre_html_mail import make_email
import re
from flask_cors import CORS
from propre_feedback import send_feedback


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
app.config["DEBUG"] = False
CORS(app)

@app.route('/')
def home():
    return render_template('api_index.html')

@app.route('/propre-api')
def propre_home():
    return render_template('api_index.html')

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
        error = {"Status": False, "Error" : "JSON Error"}
        return add_header(error)
    
    if len(files)!=len(hashes):
        error = {"Status": False, "Error" : "Different Number of Files and Hashes."}
        return add_header(error)

    if len(files)==0:
        error = {"Status": False, "Error" : "No Files Sent."}
        return add_header(error)

    email = ''
    try:
        email = data["Email ID"]
    except:
        pass
    
    try:
        results = make_tree(files, hashes)
        if "Error" in results:
            results["Status"] = False
        else:
            results["Status"] = True
    except Exception as e:
        results = {"Status": False, "Error" : str(e)}
    # print(results)
    
    try:
        if email!='' and check(email):
            make_email(email, results)
    except:
        pass

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
        error = {"Status": False, "Error" : "No Transaction ID Provided."}
        return add_header(error)

    file_hash = ''
    if 'hash' in request.args:
        file_hash = request.args['hash']
    else:
        error = {"Status": False, "Error" : "No Hash Provided."}
        return add_header(error)

    path_hash = ''
    if 'path' in request.args:
        path_hash = request.args['path']
    else:
        error = {"Status": False, "Error" : "No Path Provided."}
        return add_header(error)
    try:
        results = verify(transaction_id, file_hash, path_hash)
        if "Error" in results:
            results["Status"] = False
        else:
            results["Status"] = True
    except Exception as e:
        results = {"Status": False, "Error" : str(e)}

    results = add_header(results)

    return results

@app.route('/propre-api/feedback', methods=['GET', 'POST'])
def api_propre_feedback():

    data = request.get_json(force=True)

    first_name = ''

    if 'First Name' in data:
        first_name = data['First Name']
    else:
        error = {"Status": False, "Error" : "No First Name."}
        return add_header(error)

    last_name = ''
    if 'Last Name' in data:
        last_name = data['Last Name']
    else:
        error = {"Status": False, "Error" : "No Last Name."}
        return add_header(error)

    email_id = ''
    if 'Email ID' in data:
        email_id = data['Email ID']
    else:
        error = {"Status": False, "Error" : "No Email ID."}
        return add_header(error)

    if check(email_id)==False:
        error = {"Status": False, "Error" : "Invalid Email ID."}
        return add_header(error)

    phone_no = ''
    if 'Phone' in data:
        phone_no = data['Phone']

    feedback_text = ''
    if 'Feedback' in data:
        feedback_text = data['Feedback']
    else:
        error = {"Status": False, "Error" : "No Feedback."}
        return add_header(error)
    
    data = {
        'First Name' : first_name,
        'Last Name' : last_name,
        'Email ID' : email_id,
        'Phone' : phone_no,
        'Feedback' : feedback_text
    }

    results = {}
    try:
        send_feedback(data)
        results["Status"] = True
    except Exception as e:
        results = {"Status": False, "Error" : str(e)}

    results = add_header(results)

    return results

if __name__ == '__main__':
    app.run(threaded=True)
