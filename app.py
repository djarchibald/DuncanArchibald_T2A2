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
        lens_id = db.Column(db.Integer, primary_key = True)
        model = db.Column(db.String(50), nullable = False)
        manufacturer = db.Column(db.String(), nullable = False)
        mount = db.Column(db.String(), nullable = False)
        max_aperture = db.Column(db.String(3), nullable = False)
        focal_length = db.Column(db.String(50), nullable=False)
        owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    verified = db.Column(db.Boolean, nullable=False, default=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    lens_id = db.Column(db.Integer, db.ForeignKey('lenses.lens_id'), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

class Borrow(db.Model):
    __tablename__ = 'borrows'

    borrow_id = db.Column(db.Integer, primary_key=True)
    lens_id = db.Column(db.Integer, db.ForeignKey('lenses.lens_id'), nullable=False)
    lender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

#SCHEMAS

class LensSchema(ma.Schema):
    class Meta:
        fields = ("lens_id", "model", "manufacturer", "mount", "max_aperture", "focal_length", "owner_id")
#multiple lenses schema to handle list of lenses
lenses_schema = LensSchema(many=True)    
#single lens schema to handle lens object 
lens_schema = LensSchema()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "verified", "name", "email", "phone")
#multiple users schema
users_schema = UserSchema(many=True)
#single user schema
user_schema = UserSchema()   

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("comment_id", "user_id", "lens_id", "comment")
    
comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ("borrow_id", "lens_id", "borrower_id", "lender_id", "start_date", "end_date")

borrows_schema = BorrowSchema(many=True)
borrow_schema = BorrowSchema()


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
          max_aperture = "2.8",
          focal_length = "70-200" 
    )
    db.session.add(lens1)

    lens2 = Lens()
    lens2.model = "EF 70-300 f/4-5.6 IS II USM"     
    lens2.manufacturer = "Canon"
    lens2.mount = "EF"
    lens2.max_aperture = "4"
    lens2.focal_length = "70-300"
    
    db.session.add(lens2)

    lens3 = Lens()
    lens3.model = "RF 15-35 f/2.8L IS USM"
    lens3.manufacturer = "Canon"
    lens3.mount = "RF"
    lens3.max_aperture = "2.8"
    lens3.focal_length = "15-35"

    db.session.add(lens3)

    lens4 = Lens()
    lens4.model = "10-24 f/3.5-4.5 Di II VC HLD"
    lens4.manufacturer = "Tamron"
    lens4.mount = "EF"
    lens4.max_aperture = "3.5"
    lens4.focal_length = "10-24"

    db.session.add(lens4)

    lens5 = Lens()
    lens5.model = "AF 85 f1.4 DG HSM Art"
    lens5.manufacturer = "Sigma"
    lens5.mount = "EF"
    lens5.max_aperture = "1.4"
    lens5.focal_length = "85"

    db.session.add(lens5)

    lens6 = Lens()
    lens6.model = "XF 16-55 f2.8 R LM WR"
    lens6.manufacturer = "Fujinon"
    lens6.mount = "X"
    lens6.max_aperture = "2.8"
    lens6.focal_length = "16-55"

    db.session.add(lens6)

    lens7 = Lens()
    lens7.model = "FE 24-70 f/2.8 G Master"
    lens7.manufacturer = "Sony"
    lens7.mount = "FE"
    lens7.max_aperture = "2.8"
    lens7.focal_length = "24-70"

    db.session.add(lens7)

    lens8 = Lens()
    lens8.model = "24-70 f/2.8 DG DN Art"
    lens8.manufacturer = "Sigma"
    lens8.mount = "EF"
    lens8.max_aperture = "2.8"
    lens8.focal_length = "24-70"

    db.session.add(lens8)

    lens9 = Lens()
    lens9.model = "FE 50 f/1.4 GM"
    lens9.manufacturer = "Sony"
    lens9.mount = "FE"
    lens9.max_aperture = "1.4"
    lens9.focal_length = "50"

    db.session.add(lens9)

    lens10 = Lens()
    lens10.model = "Super-Elmar-M 18 f/3.8 ASPH"
    lens10.manufacturer = "Leica"
    lens10.mount = "M"
    lens10.max_aperture = "3.8"
    lens10.focal_length = "18"

    db.session.add(lens10)

    lens11 = Lens()
    lens11.model = "SUMMILUX-M 21 f/1.4 ASPH"
    lens11.manufacturer = "Leica"
    lens11.mount = "M"
    lens11.max_aperture = "1.4"
    lens11.focal_length = "21"

    db.session.add(lens11)

    db.session.commit()
    print ("tables seeded")

@app.cli.command("drop")
def drop_db():
     db.drop_all()
     print ("tables dropped")


#ROUTES
@app.route("/")
def index():
    return "<p>Welcome to the Lens Library!</p>"

#lists all lenses
@app.route("/lenses", methods =["GET"])
def get_lenses():
    lens_list = Lens.query.all()
    data = lenses_schema.dump(lens_list)
    return data

#single lens found by lens_id
@app.route("/lenses/<int:id>", methods=["GET"])
def get_lens(id):
    lens = Lens.query.get(id)
    data = lens_schema.dump(lens)
    return data


@app.route("/lenses", methods= ["POST"])
def post_lens():
    #receive lens fields from the flas request, use schema to load
    lens_fields = lens_schema.load(request.json)
    #accsessing lens fields

    lens = Lens(
         model = lens_fields["model"],
         manufacturer = lens_fields["manufacturer"],
         mount = lens_fields["mount"],
         max_aperture = lens_fields["max_aperture"]
    )

    db.session.add(lens)
    db.session.commit()
    return lens_schema.dump(lens)
#Lens fields received from request (from flask) & use schema to load.

    # lens_fields = lens_schema.load(request.json)
    # lens = Lens(
    #       model = lens_fields["model"],
    #       manufacturer = lens_fields["manufacturer"],
    #       mount = lens_fields["mount"],
    #       max_aperture = lens_fields["max_aperture"]
    #)

    

