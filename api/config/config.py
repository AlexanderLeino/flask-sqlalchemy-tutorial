from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from main import app

ma = Marshmallow(app)
db = SQLAlchemy(app)