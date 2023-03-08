from flask import Flask

app = Flask(__name__)

#establish connection                       dbms                db_user     pwd     URI     PORT    db_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://std2_db_dev:224245@localhost:5432/T2A2_Lens_Library"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

