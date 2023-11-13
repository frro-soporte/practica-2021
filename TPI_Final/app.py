from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect #Para proteger el login mediante un token

from config import DATABASE_CONNECTION_URI
from data.db import db
from flask_login import LoginManager

from routes.role import roles
from routes.user import users
from routes.auth import auths,status_401,status_404
from routes.location import locations
from routes.kayaktype import kayaktypes
from routes.contacts import contacts
from routes.hanger import hangers
from routes.calendarYear import calendarYears


app = Flask(__name__)


app.secret_key=b"5accdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e"

app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
login_manager = LoginManager(app)
csrf = CSRFProtect()


app.register_error_handler(401,status_401)
app.register_error_handler(404,status_404)

app.register_blueprint(auths)
app.register_blueprint(roles)
app.register_blueprint(users)
app.register_blueprint(locations)
app.register_blueprint(kayaktypes)
app.register_blueprint(contacts)
app.register_blueprint(hangers)
app.register_blueprint(calendarYears)

