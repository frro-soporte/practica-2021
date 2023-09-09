from data.db import db
from datetime import datetime

class location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    createDate = db.Column(db.DateTime, nullable=False)
    finalDate = db.Column(db.DateTime)
    state = db.Column(db.Integer)

    def __init__(self,userId, name, description, state = 1):
        self.userId = userId
        self.name = name
        self.description = description
        self.createDate = datetime.now()
        self.state = state