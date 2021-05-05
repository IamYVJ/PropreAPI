import flask
from flask import request, jsonify
from propre_tree import make_tree
import re
from propre_mail import make_email

def check(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
        return False

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/propre/api', methods=['GET', 'POST'])
def api_propre():

    files = []

    if 'files' in request.args:
        files = request.args['files'].split()
    else:
        return "Error: No Files Provided."

    hashes = []
    if 'hashes' in request.args:
        hashes = request.args['hashes'].split()
    else:
        return "Error: No Files Provided." 

    if len(files)!=len(hashes):
        return "Error: Different Number of Files and Hashes."


    email = ''
    if 'email' in request.args:
        email = request.args['email']

    results = make_tree(files, hashes)

    if email!='' and check(email):
        make_email(email, results)

    results = jsonify(results)

    results.headers.add("Access-Control-Allow-Origin", "*")

    return results
    # return jsonify(results)

if __name__ == '__main__':
    app.run(threaded=True)
