from data.db import db
from datetime import datetime

class quota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    calendarId = db.Column(db.Integer, db.ForeignKey('calendaryear.id'), nullable=False)
    quota = db.Column(db.Integer, nullable = False)
    createDate = db.Column(db.DateTime, nullable=False)
    finalDate = db.Column(db.DateTime)
    state = db.Column(db.Integer)
    
    def _init_(self,userId, calendarId, quota, state = 1):
        self.userId = userId
        self.calendarId = calendarId
        self.quota = quota
        self.createDate = datetime.now()
        self.state = state