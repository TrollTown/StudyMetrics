from app import flask_app

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',debug=True, port = 50000, use_reloader=True)
    flask_app.logger.error("THIS IS IN RUN.PY")