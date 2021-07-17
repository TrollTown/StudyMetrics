#!/usr/bin/env python3
from flask import jsonify, request
from app import flask_app
import json, os
from app.whiteboard import save_canvas, load_canvas
from app.dbtools import *
from passlib.hash import pbkdf2_sha512

@flask_app.route('/', methods=['GET'])
def root():
    return jsonify({'response' : 'Hello'}), 200

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    content = request.json
    print(content)
    name = content['name']
    print(name)
    email = content['email']
    print(email)
    password = content['password']
    print(password)
    userType = content['userType']
    print(userType)
    users = getUserByEmail(email)
    isTeacher = None
    if len(users) != 0:
        return jsonify({"result" : "failed", "reason" : "Email is already registered."}, 400)
    else:
        pw_hash = pbkdf2_sha512.hash(password)
        if userType == "student":
            isTeacher = False
        else:
            isTeacher = True
        insertUserIntoDatabase(name, email, pw_hash, isTeacher)
        return jsonify({"result" : "success"})

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    pass

#Nathan: code for saving students' whiteboard
# what do i put for the url??
@flask_app.route("/save_whiteboard", methods=['GET', 'POST'])
def submit_canvas_from_database():
    payload = request.get_json()
    resp = save_canvas(payload['canvas_id'], payload['canvas_coordinates']) # save_canvas function saves to database
    # dump_data()
    return json.dumps(resp)

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
    resp = updateHistory(payload['questionID'], payload['studentID'], payload['answer'], payload['workingOutPhoto']) # load_canvas grabs array from database
    


    # dump_data()
    return json.dumps(resp)