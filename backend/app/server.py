#!/usr/bin/env python3
from app.clienttools import approveAnswer, getEntireLevelProgress
from flask import jsonify, request, render_template
from app import flask_app
import json, os
from app.dbtools import *
from app.clienttools import *
from app.history import *
from app.spaced_repetition import *
from passlib.hash import pbkdf2_sha512
import sys

@flask_app.route('/', methods=['GET'])
def root():
    flask_app.logger.error("ROOT LOG")
    return jsonify({'response' : 'Hello'}), 200

@flask_app.route('/register', methods=['POST'])
def register():
    content = request.json
    flask_app.logger.error(str(content))
    name = content['name']
    email = content['email']
    password = content['password']
    userType = content['userType']
    users = getUserByEmail(email)
    flask_app.logger.error(users)
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
        userInfo = getUserByEmail(email)
        userid = userInfo[0][0]
        return jsonify({"result" : "success", "token" : userid}), 200

@flask_app.route('/login', methods=['POST'])
def login():
    content = request.json
    flask_app.logger.error(str(content))
    email = content['email']
    password = content['password']
    users = getUserByEmail(email)
    flask_app.logger.error(users)
    if len(users) != 1:
        return jsonify({"result" : "failed", "reason" : "Login failed"}),400
    stored_hash = users[0][3]
    if pbkdf2_sha512.verify(password, stored_hash):
        return jsonify({"result" : "success", "token" : users[0][0]}), 200
    else:
        return jsonify({"result" : "failed", "reason" : "Login failed"}), 400

#get question
@flask_app.route("/get_question_by_ID", methods=['GET'])
def get_question_by_ID():
    questionID = request.args.get('questionID')
    flask_app.logger.error(questionID)
    resp = getQuestionDataByID(questionID)
    flask_app.logger.error(resp)
    questionText = resp['questionText']
    questionTextSplit = questionText.split(' ')
    answer = questionTextSplit[-1].split('|')
    resp['questionText'] = ' '.join(questionTextSplit[0:-1])[:-1]
    resp['options'] = answer[1:-1]
    return json.dumps(resp)


@flask_app.route("/get_subject_by_ID", methods=['GET'])
def get_subject_by_ID():
    subjectID = request.args.get('subjectID')
    resp = getSubjectDataByID(subjectID)
    return json.dumps(resp)

@flask_app.route("/get_module_by_ID", methods=['GET'])
def get_module_by_ID():
    moduleID = request.args.get('moduleID')
    resp = getModuleDataByID(moduleID)
    return json.dumps(resp)

@flask_app.route("/get_submodule_by_ID", methods=['GET'])
def get_submodule_by_ID():
    submoduleID = request.args.get('submoduleID')
    resp = getSubmoduleDataByID(submoduleID)
    return json.dumps(resp)

#get list of unapproved questions
@flask_app.route("/get_unapproved_questions", methods=['GET'])
def get_unapproved_questions():
    teacherID = request.args.get('teacherID')
    resp = getUnapprovedQuestions(teacherID)
    return json.dumps(resp)

#get list of curated training questions
@flask_app.route("/get_revision_questions", methods=['GET'])
def get_revision_questions():
    resp = selectRevisionQ(request.args.get('studentID'))
    return json.dumps(resp)

#approve old answers
@flask_app.route("/approve_answer", methods=['GET'])
def approve_answer():
    payload = request.get_json()
    resp = approveAnswer(payload['questionID'],payload['studentID'],payload['finish_time'],payload['result'])
    return json.dumps(resp)

#get stats for student
@flask_app.route("/get_stats_by_ID", methods=['GET'])
def get_stats_by_ID():
    resp = radarGraphForStudent(request.args.get('studentID'), request.args.get('searchValue'), request.args.get('searchMode')) 
    return json.dumps(resp)

#get stats for student
@flask_app.route("/get_class_members", methods=['GET'])
def get_class_members():
    payload = request.get_json()
    resp = getClassMembers(payload['classID']) 
    return json.dumps(resp)

#get stats for student
@flask_app.route("/get_class_list", methods=['GET'])
def get_class_list():
    resp = getClassList(request.args.get('teacherID'))
    return json.dumps(resp)

#submit question
@flask_app.route("/upload_question", methods=['POST'])
def upload_question():
    payload = request.get_json()
    # need to update history 
    # load_canvas grabs array from database
    uploadQuestion(payload['subjectID'],payload['moduleID'],payload['submoduleID'],payload['questionText'],payload['questionType'],payload['answer'],payload['photo'],payload['difficulty'],payload['authorID'])

    # dump_data()
    return json.dumps({'result':'success'})

# Question submission
@flask_app.route("/submit_answer", methods=['POST'])
def submit_answer():
    payload = request.get_json()
    # need to update history 
    resp = updateHistory(payload['questionID'], payload['studentID'], payload['answer']) # load_canvas grabs array from database

    # dump_data()
    return json.dumps(resp)

# Get the next question to do
@flask_app.route("/get_next_question", methods=['GET'])
def get_next_question():
    # need to update history 
    resp = getNextQuestion(request.args.get('studentID'), request.args.get('submoduleID')) # load_canvas grabs array from database

    # dump_data()
    return json.dumps(resp)$

# Get the next question to do
@flask_app.route("/get_entire_level_progress", methods=['GET'])
def get_entire_level_progress():
    payload = request.get_json()
    # need to update history 
    resp = getEntireLevelProgress(payload['studentID'], payload['levelType'],payload['parentLevelID']) # load_canvas grabs array from database

    # dump_data()
    return json.dumps(resp)


@flask_app.route("/get_class_radar", methods=['GET'])
def get_class_radar():
    payload = request.get_json()
    # need to update history 
    resp = getClassRadar(payload['classID']) # load_canvas grabs array from database

    # dump_data()
    return json.dumps(resp)

@flask_app.route("/get_class_list_by_student_ID", methods=['GET'])
def get_class_list_by_student_ID():
    payload = request.get_json()
    # need to update history 
    resp = getClassListByStudentID(payload['studentID']) # load_canvas grabs array from database

    # dump_data()
    return json.dumps(resp)