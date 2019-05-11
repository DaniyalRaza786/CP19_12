import flask
from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('page.html')
@app.route("/Taha")
def Taha():
    return "Hello taha!"
app.run(debug=True)