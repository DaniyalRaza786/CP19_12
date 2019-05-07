import flask
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def Taha():
    return "Hello Taha!"
@app.route("/daniyal")
def Daniyal():
    return "Hello Daniyal!"
app.run()