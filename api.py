import flask
from flask import request, jsonify
from propre_tree import make_tree

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

    results = make_tree(files, hashes)

    return results
    # return jsonify(results)

app.run()
