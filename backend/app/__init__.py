from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
flask_app = Flask(__name__)
flask_app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")

from app import server