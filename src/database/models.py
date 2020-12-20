from .db import db

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    age = db.IntField(unique=True)