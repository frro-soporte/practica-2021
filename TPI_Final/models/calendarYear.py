from data.db import db

class calendarYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    yearCalendar = db.Column(db.Integer)
    description = db.Column(db.String(250))
    createDate = db.Column(db.DateTime, nullable=False)
    finalDate = db.Column(db.DateTime)
    state = db.Column(db.Integer)

def __init__(self, userId, yearCalendar ,description,createDate, finalDate, state):
    
    self.userId = userId
    self.yearCalendar = yearCalendar
    self. description = description
    self.createDate = createDate
    self.finalDate = finalDate
    self.state = state