from . import db
from flask_login import UserMixin

class Bungalow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(255), unique=True)
    type = db.Column(db.Integer, db.ForeignKey('bungalowtype.id'))

    bungalow_type = db.relationship('Bungalowtype', back_populates='bungalows')

class Bungalowtype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aantal_personen = db.Column(db.Integer)
    weekprijs = db.Column(db.Float)

    bungalows = db.relationship('Bungalow', back_populates='bungalow_type')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

