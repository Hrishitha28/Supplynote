# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.path.dirname(__file__), '../config.py'))
db = SQLAlchemy(app)

from app import routes  # Import routes after creating app and db objects

# Note: This import is placed at the end to avoid circular imports
