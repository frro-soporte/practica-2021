from data.db import db

class role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    state = db.Column(db.Integer)

    # Relaciones
    # usr = db.relationship('user',uselist=False,back_populates="role",cascade="all, delete-orphan",single_parent=True)

    def __init__(self, name, description, state):
        self.name = name
        self.description = description
        self.state = state