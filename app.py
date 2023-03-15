from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#CONFIG

app = Flask(__name__)

#establish connection                       dbms                db_user     pwd     URI     PORT    db_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://std2_db_dev:224245@localhost:5432/t2a2_lens_library"
db = SQLAlchemy(app)
ma = Marshmallow(app)

#MODELS
class Lens (db.Model):
       #tablename
        __tablename__ = "lenses"
        #primary key
        lens_id = db.Column(db.Integer, primary_key = True)
        #attributes
        model = db.Column(db.String(50))
        manufacturer = db.Column(db.String())
        mount = db.Column(db.String())
        max_aperture = db.Column(db.String(3))

#SCHEMAS

#class LensSchema(ma.Schema):
    #class Meta:
     #    fields = ("lens_id", "model", "manufacturer", "mount", "max_aperture")
#multiple lenses schema to handle list of lenses
#lenses_schema = LensSchema(many=True)    
#single lens schema to handle lens object 
#lens_schema = LensSchema()
         

#CLI COMMANDS

@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created!")

@app.cli.command("seed")
def seed_db():
    lens1 = Lens(
          model = "RF 70-200 f/2.8L IS USM",
          manufacturer = "Canon",
          mount = "RF",
          max_aperture ="2.8" 
    )
    db.session.add(lens1)

    lens2 = Lens()
    lens2.model = "EF 70-300 f/4-5.6 IS II USM"     
    lens2.manufacturer = "Canon"
    lens2.mount = "EF"
    lens2.max_aperture = "4"
    
    db.session.add(lens2)
     
    db.session.commit()
    print ("tables seeded")

    #  lens_list = Lens[
    #     ("RF 70-200 f/2.8L IS USM", "Canon", "RF", "2.8"),
    #     ("EF 70-300mm f/4-5.6 IS II USM", "Canon", "EF", "4"),
    #     ("RF 15-35mm f/2.8L IS USM", "Canon", "RF", "2.8"),
    #     ("10-24mm f/3.5-4.5 Di II VC HLD", "Tamron", "EF", "3.5"),
    #     ("AF 85mm F1.4 DG HSM Art", "Sigma", "EF", "1.4"),
    #     ("XF16-55mm F2.8 R LM WR", "Fujinon", "X", "2.8"),
    #     ("FE 24-70mm f/2.8 G Master", "Sony", "FE", "2.8"),
    #     ("24-70mm f/2.8 DG DN Art", "Sigma", "EF", "2.8"),
    #     ("FE 50mm f/1.4 GM", "Sony", "FE", "1.4"),
    #     ("Super-Elmar-M 18mm f/3.8 ASPH", "Leica", "M", "3.8"),
    #     ("SUMMILUX-M 21 f/1.4 ASPH", "Leica", "M", "1.4")
    # ]
     
     

    
#ROUTES
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#lists all lenses
#@app.route("/lenses", methods =["GET"])
#def get_lenses():
#     lens_list = Lens.query.all()
#    data = lenses_schema.dump(lens_list)
#     return data
#single lens found by lens_id
#@app.route("/lenses/<int:id>", methods=["GET"])
#def get_lens(id):
#    lens = Lens.query.get(id)
#    data = lens_schema.dump(lens)
#    return data

#@app.route("/books", methods= ["POST"])
#def post_lens():
#Lens fields received from request (from flask) & use schema to load.

#    lens_fields = lens_schema.load(request.json)
#    lens = Lens(
#          model = lens_fields["model"],
#          manufacturer = lens_fields["manufacturer"],
#          mount = lens_fields["mount"],
#          max_aperture = lens_fields["max_aperture"]
#    )

#db.session.add(lens)
#db.session.commit()
#return lens_schema.dump(lens)