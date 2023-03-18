from app import ma

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ("borrow_id", "lens_id", "borrower_id", "lender_id", "start_date", "end_date")

borrows_schema = BorrowSchema(many=True)
borrow_schema = BorrowSchema()