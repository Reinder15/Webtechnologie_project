from . import db
from flask_login import UserMixin

class Huisje():
    id = db.collumn(db.integer, primary_key=True)
    naam = db.collumn(db.string(255))
    type = db.collumn(db.integer)

class User(db.model, UserMixin):
    id = db.Collumn(db.integer, primary_key=True)
    email = db.collumn(db.string(255), unique=True)
    password = db.cullumn(db.string(255))

