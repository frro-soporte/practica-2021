from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DATABASE_CONNECTION_URI
from data.db import db

from routes.role import roles

app = Flask(__name__)

app.secret_key="tpi"

app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

app.register_blueprint(roles)