from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hola mundo desde aqui'

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return 'Hello app'

@app.route("/say")
def say():
    name = 'Grace'
    return f'Hi {name}'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)