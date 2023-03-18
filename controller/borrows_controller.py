from flask import Blueprint, jsonify, request
from model.borrow import Borrow
from schema.borrows_schema import borrow_schema, borrows_schema
from app import db

borrow = Blueprint('borrow', __name__, url_prefix="/borrows")

@borrow.get("/")
def get_borrows():
    borrows = Borrow.query.all()
    return borrows_schema.dump(borrows) 

@borrow.get("/<int:id>")
def get_borrow(id):
    borrow = Borrow.query.get(id)
    
    if not borrow:
        return {"message": "I can't find that borrow transaction"}
    
    return borrow_schema.dump(borrow)

@borrow.post("/")
def create_borrow():
    try:
        borrow_fields = borrow_schema.load(request.json)

        borrow = Borrow(**borrow_fields)
           
        db.session.add(borrow)
        db.session.commit()
    except:
        return {"message": "Hmm. I can't seem to create that borrow transaction. Check the information is correct." }
    
    return borrow_schema.dump(borrow)