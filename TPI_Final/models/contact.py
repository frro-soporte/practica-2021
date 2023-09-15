from data.db import db
from datetime import datetime

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(250))
    phone = db.Column(db.String(50))
    description = db.Column(db.String(250))
    createDate = db.Column(db.DateTime, nullable=False)
    finalDate = db.Column(db.DateTime)
    state = db.Column(db.Integer)

def __init__(self, fullname, email, phone, description,createDate, finalDate, state):
    self.fullname = fullname
    self.email = email
    self.phone = phone
    self. description = description
    self.createDate = createDate
    self.finalDate = finalDate
    self.state = state