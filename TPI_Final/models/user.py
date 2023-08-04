from werkzeug.security import generate_password_hash
from flask_login import UserMixin

from data.db import db

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    roleId = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(250), nullable=False)
    docNumber = db.Column(db.String(250), nullable=False)
    mail = db.Column(db.String(250), nullable=False)
    userName = db.Column(db.String(100), nullable=False)
    userPass = db.Column(db.String(250), nullable=False)
    state = db.Column(db.Integer)

    # Relaciones
    # role = db.relationship('role', back_populates="user", single_parent=True, cascade="all,delete-orphan")

    def __init__(self, roleId, firstName, lastName, address, phone, docNumber, mail, userName, userPass, state):
        self.roleId = roleId
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.phone = phone
        self.docNumber = docNumber
        self.mail = mail
        self.userName = userName
        self.userPass = generate_password_hash(userPass)
        self.state = state