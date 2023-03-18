from app import db

class Lens (db.Model):
       #tablename
        __tablename__ = "lenses"
        lens_id = db.Column(db.Integer(), primary_key = True)
        model = db.Column(db.String(), nullable = False)
        manufacturer = db.Column(db.String(), nullable = False)
        mount = db.Column(db.String(), nullable = False)
        max_aperture = db.Column(db.String(), nullable = False)
        owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)