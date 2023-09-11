from data.db import db
from datetime import datetime

class calendaryear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    yearCalendar = db.Column(db.Integer)
    description = db.Column(db.String(250))
    createDate = db.Column(db.DateTime, nullable=False)
    finalDate = db.Column(db.DateTime)
    state = db.Column(db.Integer)

    def _init_(self,userId, yearCalendar, description, state = 1):
        self.userId = userId
        self.name = yearCalendar
        self.description = description
        self.createDate = datetime.now()
        self.state = state