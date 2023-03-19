from app import db


class Borrow(db.Model):
    __tablename__ = 'borrows'

    borrow_id = db.Column(db.Integer(), primary_key=True)
    lens_id = db.Column(db.Integer(), db.ForeignKey('lenses.lens_id'), nullable=False)
    lender_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'), nullable=False)
    borrower_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

