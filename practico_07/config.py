import os
from dotenv import load_dotenv  # Instalar con pip install python-dotenv

load_dotenv()  # Carga todo el contenido de .env en variables de entorno

class Config:
    SERVER_NAME = "localhost:7001"
    DEBUG = True
    DB_TOKEN = os.environ.get("DB_TOKEN", "")
    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
    TEMPLATES_AUTO_RELOAD = True
    DATABASE_PATH = "app/database/contact_book.db"