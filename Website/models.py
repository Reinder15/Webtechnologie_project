from . import db
from flask_login import UserMixin

class Bungalow(db.model):
    id = db.collumn(db.integer, primary_key=True)
    naam = db.collumn(db.string(255), unique=True)
    type = db.collumn(db.integer, db.ForeignKey('bungalowtype.id'))

    bungalow_type = db.relationship('Bungalowtype', back_populates='bungalows')

class Bungalowtype(db.model):
    id = db.collumn(db.integer, primary_key=True)
    aantal_personen = db.collumn(db.integer)
    weekprijs = db.collumn(db.float)

    bungalows = db.relationship('Bungalow', back_populates='bungalow_type')

class User(db.model, UserMixin):
    id = db.Collumn(db.integer, primary_key=True)
    email = db.collumn(db.string(255), unique=True)
    password = db.cullumn(db.string(255))

