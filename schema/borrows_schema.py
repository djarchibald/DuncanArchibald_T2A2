from app import ma


class BorrowSchema(ma.Schema):
    class Meta:
        fields = ("borrow_id", "lens_id", "borrower_id", "lender_id", "start_date", "end_date", "lenses")

    
    user = ma.Nested("UserSchema")
    lens = ma.Nested("LensSchema")
    start_date = ma.DateTime(format="%Y-%m-%d")
    end_date = ma.DateTime(format="%Y-%m-%d")

borrows_schema = BorrowSchema(many=True)
borrow_schema = BorrowSchema()