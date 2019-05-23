import pyrebase
config={
"apiKey": "AIzaSyDYt-fmafI1kkMZSIphL829C6QgdlE1Tro",
    "authDomain": "cp19-12.firebaseapp.com",
    "databaseURL": "https://cp19-12.firebaseio.com",
   " projectId": "cp19-12",
    "storageBucket": "cp19-12.appspot.com",
    "messagingSenderId": "681358965828",
    "appId": "1:681358965828:web:3e31fb7429aed930"

}
firebase = pyrebase.initialize_app(config)

db = firebase.database()
storage=firebase.storage()
import flask
from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def hello():
   new_post=db.child("names").get()
   user=new_post.val()
   l=user.key()
   return l
@app.route("/Taha")
def Taha():
    return "Hello taha!"
@app.route("/Daniyal")
def Daniyal():
    return "Hello Daniyal"
@app.route("/fahad")
def fahad():
    return "Hello fahad"
app.run(debug=True)