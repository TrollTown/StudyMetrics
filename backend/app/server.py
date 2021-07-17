#!/usr/bin/env python3
from flask import jsonify, request
from app import flask_app
import json
from app.whiteboard import save_canvas, load_canvas

@flask_app.route('/', methods=['GET'])
def root():
    return jsonify({'response' : 'Hello'}), 200

#Nathan: code for saving students' whiteboard
# what do i put for the url??
@flask_app.route("/save_whiteboard", methods=['POST'])
def submit_canvas_from_database():
    payload = request.get_json()
    resp = save_canvas(payload['canvas_id'], payload['canvas_coordinates']) # save_canvas function saves to database
    # dump_data()
    return json.dumps(resp)

#Nathan: code for loading a saved whiteboard
# what do i put for the url??
@flask_app.route("/load_whiteboard", methods=['POST'])
def load_canvas_from_database():
    payload = request.get_json()
    resp = load_canvas(payload['canvas_id']) # load_canvas grabs array from database
    # dump_data()
    return json.dumps(resp)