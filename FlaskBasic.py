import flask
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def World():
    return "Hello World!"

@app.route("/taha")
def Taha():
    return "Hello Taha!"
@app.route("/daniyal")
def Daniyal():
    return "Hello Daniyal!"
app.run(debug=True)