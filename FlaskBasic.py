import flask
from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World'
@app.route("/Taha")
def Taha():
    return "Hello taha!"
@app.route("/Daniyal")
def Daniyal():
    return "Hello Daniyal"
app.run(debug=True)