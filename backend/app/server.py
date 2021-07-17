#!/usr/bin/env python3
from flask import jsonify
from app import flask_app

@flask_app.route('/', methods=['GET'])
def root():
    return jsonify({'response' : 'Hello'}), 200