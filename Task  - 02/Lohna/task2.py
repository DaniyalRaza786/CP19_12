import flask
from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def Lohna():
    return "Hello Lohna!"
app.run()