#!/usr/bin/env python3
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
flask_app = Flask(__name__)
flask_app.config["SECRET_KEY"] = FLASK_SECRET_KEY

@flask_app.route('/', methods=['GET'])
def root():
    return jsonify({'response' : 'Hello'}), 200

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
