from flask import Flask
from config import Config
from .database.connection import reset_table

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
reset_table()


# Estos imports tiene que estar abajo para evitar referencias circulares

from . import routes  
from . import errors  
