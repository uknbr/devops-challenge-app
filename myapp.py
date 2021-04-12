import os
import platform
import pyjokes
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
	result = {"status": "not found"}
	return jsonify(result), 404

@app.route('/code')
def code():
	_env = os.getenv("CODE", "")
	if _env:
		result = {"code": _env}
		return jsonify(result), 200
	else:
		result = {"code": "ERROR"}
		return jsonify(result), 500

@app.route('/ping')
def ping():
	_name = os.getenv("NAME", "")
	if _name:
		result = {"status": "pong"}
		return jsonify(result), 200
	else:
		result = {"status": "ERROR"}
		return jsonify(result), 503

@app.route('/stat')
def stat():
	_name = os.getenv("NAME", "")
	_host = platform.node()
	_joke = pyjokes.get_joke()

	result = {"name": _name, "host": _host, "joke": _joke}
	return jsonify(result), 200

if __name__ == '__main__':
	app.run(use_reloader=True, host='0.0.0.0', port=3535, debug=True)
