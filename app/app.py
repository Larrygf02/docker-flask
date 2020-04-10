from flask import Flask, render_template, requestm jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

## Config DB
DB_URL = 'postgresql+psycopg2://postgres:P3n1p@P0stgr3@172.16.24.16/staging'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)

## Class
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(Integer, primary_key=True, server_default=text("nextval('persons_id_seq'::regclass)"))
    name = db.Column(db.String(50))
    edad = db.Column(db.Integer)

@app.route("/")
def index():
    return 'Hola mundo'

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/person", methods["POST"])
def postPerson():
    parametros = request.get_json()
    new_person = Person(**parametros)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"status": True, "response": "Agregado correctamente"})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')