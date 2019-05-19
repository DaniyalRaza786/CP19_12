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

#from flask import Flask , render_template,*
from flask import *
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def hello():
    if request.method=='POST':
        name=request.form['feed']
        images=request.files['picture']
        if name != "":
             db.child("new_post").push(name)
             new_post=db.child("new_post").get()
             new=new_post.val()
             return render_template('Home.html',post=new.values())
        if images != "":
             storage.child("image/new.jpg").put(images)
             link=storage.child("image").get_url(None)
             return render_template('Home.html',l=link)
        
    new_post=db.child("new_post").get()
    new=new_post.val()
    link=storage.child("image/new1.jpg").get_url(None)
    return render_template('Home.html',post=new.values(),l=link)
    
@app.route("/Taha")
def Taha():
    return "Hello taha!"
app.run(debug=True)