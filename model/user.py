from app import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True)
    verified = db.Column(db.Boolean, nullable=False, default=False)
    name = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)