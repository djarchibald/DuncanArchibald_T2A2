from app import db

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'), nullable=False)
    lens_id = db.Column(db.Integer(), db.ForeignKey('lenses.lens_id'), nullable=False)
    comment = db.Column(db.String(), nullable=False)