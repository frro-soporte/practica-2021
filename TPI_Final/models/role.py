from data.db import db

class role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    state = db.Column(db.Integer)

    def __init__(self, name, description, state):
        self.name = name
        self.description = description
        self.state = state