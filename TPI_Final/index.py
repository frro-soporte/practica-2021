from models.auth import get_user
from app import app
from data.db import db
from app import login_manager

from models.user import user

import config
@login_manager.user_loader
def load_user(id):
    return get_user(id)

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True);