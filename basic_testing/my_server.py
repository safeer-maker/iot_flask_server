import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route("/query", methods=['GET'])
def query():
    name = request.args.get('name')
    arg = request.args.get('sss')

    return jsonify(
        name, arg
    )
app.run(host = '0.0.0.0')