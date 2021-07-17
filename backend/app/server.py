#!/usr/bin/env python3
from flask import jsonify, request, render_template
from app import flask_app
import json, os
from app.dbtools import *
from passlib.hash import pbkdf2_sha512
import sys

@flask_app.route('/', methods=['GET'])
def root():
    flask_app.logger.error("ROOT LOG")
    return jsonify({'response' : 'Hello'}), 200

@flask_app.route('/register', methods=['POST'])
def register():
    flask_app.logger.error("BEFORE HELLLLOOOOOO")
    flask_app.logger.error(str(request))
    content = request.json
    flask_app.logger.error(str(content))
    flask_app.logger.error(str("12345678"))
    name = content['name']
    flask_app.logger.error(name)
    email = content['email']
    flask_app.logger.error(email)
    password = content['password']
    flask_app.logger.error(password)
    userType = content['userType']
    flask_app.logger.error(userType)
    flask_app.logger.error("HELLLLOOOOOO")
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

@flask_app.errorhandler(500)
def internal_error(exception):
    flask_app.logger.error(exception)
    return render_template('500.html'), 500

@flask_app.route('/login', methods=['POST'])
def login():
    pass

#get question
@flask_app.route("/get_question_by_ID", methods=['GET'])
def get_question():
    pass

# Question submission
@flask_app.route("/submit_question", methods=['POST'])
def submit_question():
    payload = request.get_json()
    # need to update history 
    resp = updateHistory(payload['questionID'], payload['studentID'], payload['answer']) # load_canvas grabs array from database

    # dump_data()
    return json.dumps(resp)