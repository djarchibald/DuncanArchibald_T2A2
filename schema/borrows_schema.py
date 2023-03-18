from app import ma
from marshmallow import fields

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ("borrow_id", "lens_id", "borrower_id", "lender_id", "start_date", "end_date")

    user = fields.Nested("UserSchema")
    lens = fields.Nested("LensSchema")
    start_date = fields.DateTime(format="%Y-%m-%d")
    end_date = fields.DateTime(format="%Y-%m-%d")

borrows_schema = BorrowSchema(many=True)
borrow_schema = BorrowSchema()