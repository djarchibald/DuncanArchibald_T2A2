from flask import Blueprint, jsonify, request
from model.lens import Lens
from schema.lenses_schema import lens_schema, lenses_schema
from app import db

lens = Blueprint('lens', __name__, url_prefix="/lenses")

@lens.get("/")
def get_lenses():
    lenses = Lens.query.all()
    return lenses_schema.dump(lenses) 

@lens.get("/<int:id>")
def get_lens(id):
    lens = Lens.query.get(id)
    
    if not lens:
        return {"message": "That lens isn't in the library"}
    
    return lens_schema.dump(lens)

@lens.post("/")
def create_lens():
    # try:
        lens_fields = lens_schema.load(request.json)

        lens = Lens(**lens_fields)
           
        db.session.add(lens)
        db.session.commit()
    # except:
    #     return {"message": "Your information is incorrect" }
    
        return lens_schema.dump(lens)