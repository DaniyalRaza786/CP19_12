import flask
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def Taha():
    return "Hello Taha!"
app.run()