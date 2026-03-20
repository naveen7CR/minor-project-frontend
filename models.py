# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     stars = db.Column(db.Integer, default=0)

# class Mentor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     subject = db.Column(db.String(100))
#     stars = db.Column(db.Integer)

# class Chat(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user = db.Column(db.String(100))
#     mentor = db.Column(db.String(100))
#     message = db.Column(db.String(500))