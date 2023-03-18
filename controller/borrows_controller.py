from flask import Blueprint
from model.borrow import Borrow
from schema.borrows_schema import borrow_schema, borrows_schema

borrow = Blueprint('borrow', __name__, url_prefix="/borrows")

@borrow.get("/")
def get_borrows():
    borrows = Borrow.query.all()
    return borrows_schema.dump(borrows) 