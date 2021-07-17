from app import flask_app
from backend.whiteboard import save_canvas, load_canvas

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',debug=True, port = 50000, use_reloader=True)

#Nathan: code for saving students' whiteboard
# what do i put for the url??
@APP.route("/save_whiteboard", methods=['POST'])
def get_canvas_from_web():
    payload = request.get_json()
    resp = save_canvas(payload['canvas_id'], payload['data_URL']) # save_canvas function saves to database
                                                                  # Front end will have to convert image to string
                                                                  # var data_URL = canvas.toDataURL('image/jpeg', 1.0);
    dump_data()
    return dumps(resp)

#Nathan: code for loading a saved whiteboard
# what do i put for the url??
@APP.route("/load_whiteboard", methods=['POST'])
def load_canvas():
    payload = request.get_json()
    resp = load_canvas(payload['canvas_id']) # load_canvas grabs data_URL from database
    dump_data()
    return dumps(resp)