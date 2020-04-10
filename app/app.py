from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## Config DB
DB_URL = 'postgresql+psycopg2://postgres:123@db/crudperson'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123@localhost:5432/crudperson'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

## Class
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('persons_id_seq'::regclass)"))
    name = db.Column(db.String(50))
    edad = db.Column(db.Integer)

@app.route("/")
def index():
    return 'Hola mundo'

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/person", methods=["POST"])
def postPerson():
    parametros = request.get_json()
    new_person = Person(**parametros)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"status": True, "response": "Agregado correctamente"})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')