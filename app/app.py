from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hola mundo'

@app.route("/home")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')