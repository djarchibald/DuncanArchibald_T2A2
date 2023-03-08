from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

#CONFIG

app = Flask(__name__)

#establish connection                       dbms                db_user     pwd     URI     PORT    db_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://std2_db_dev:224245@localhost:5432/T2A2_Lens_Library"
db = SQLAlchemy(app)

#MODELS
class Lens (db.Model):
       #tablename
        __tablename__ = "lenses"
        #primary key
        lens_id = db.Column(db.Integer, primary_key = True)
        #attributes
        model = db.Column(db.Varchar(50))
        manufacturer = db.Column(db.String())
        mount = db.Column(db.String())
        max_aperture = db.Column(db.Varchar(3))


#CLI COMMANDS

@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created!")

@app.cli.command("seed")
def seed_db():
     lens = Lens(
          
     )

#ROUTES
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/lenses", methods =["GET"])
def get_lenses():
     lens_list = Lens.query.all()
     return jsonify(lens_list)
