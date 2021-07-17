#!/usr/bin/env python3
from flask import jsonify, request
from app import flask_app
import json, os
from app.dbtools import *
from passlib.hash import pbkdf2_sha512
import sys

@flask_app.route('/', methods=['GET'])
def root():
    return jsonify({'response' : 'Hello'}), 200

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    content = request.json
    flask_app.logger.error("HELLLLOOOOOO")
    name = content['name']
    flask_app.logger.error(name)
    email = content['email']
    flask_app.logger.error(email)
    password = content['password']
    flask_app.logger.error(password)
    userType = content['userType']
    flask_app.logger.error(userType)
    users = getUserByEmail(email)
    isTeacher = None
    if len(users) != 0:
        return jsonify({"result" : "failed", "reason" : "Email is already registered."}),400
    else:
        pw_hash = pbkdf2_sha512.hash(password)
        if userType == "student":
            isTeacher = False
        else:
            isTeacher = True
        insertUserIntoDatabase(name, email, pw_hash, isTeacher)
        return jsonify({"result" : "success"}), 200

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    pass


#Nathan: code for loading a saved whiteboard
# what do i put for the url??
@flask_app.route("/load_whiteboard", methods=['GET', 'POST'])
def load_canvas_from_database():
    payload = request.get_json()
    resp = load_canvas(payload['canvas_id']) # load_canvas grabs array from database
    # dump_data()
    return json.dumps(resp)

# Question submission
@flask_app.route("/submit_question", methods=['POST'])
def submit_question():
    payload = request.get_json()
    # need to update history 
    resp = updateHistory(payload['questionID'], payload['studentID'], payload['answer']) # load_canvas grabs array from database
    

    # dump_data()
    return json.dumps(resp)