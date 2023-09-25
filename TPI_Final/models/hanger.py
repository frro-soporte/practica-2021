from data.db import db

class hanger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    locationId = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    nroHanger = db.Column(db.Integer)
    description = db.Column(db.String(250))
    createDate = db.Column(db.DateTime, nullable=False)
    finalDate = db.Column(db.DateTime)
    state = db.Column(db.Integer)

def __init__(self, userId, locationId, nroHanger ,description,createDate, finalDate, state):
    
    self.userId = userId
    self.locationId = locationId
    self.nroHanger = nroHanger
    self. description = description
    self.createDate = createDate
    self.finalDate = finalDate
    self.state = state