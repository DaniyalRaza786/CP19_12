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

#from flask import Flask , render_template,*
from flask import *
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def hello():
    if request.method=='POST':
        name=request.form['feed']
        db.child("new_post").push(name)
        new_post=db.child("new_post").get()
        new=new_post.val()
        return render_template('Home.html',post=new.values())
    new_post=db.child("new_post").get()
    new=new_post.val()
    return render_template('Home.html',post=new.values())
@app.route("/Taha")
def Taha():
    return "Hello taha!"
app.run(debug=True)