from sqlalchemy import Column, Table
# from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash
# from config import engine


db = SQLAlchemy()

class mdl_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

userTable = Table('mdl_user', mdl_user.metadata)
