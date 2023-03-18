from flask import Blueprint
from model.lens import Lens
from schema.lenses_schema import lens_schema, lenses_schema

lens = Blueprint('lens', __name__, url_prefix="/lenses")

@lens.get("/")
def get_lenses():
    lenses = Lens.query.all()
    return lenses_schema.dump(lenses) 