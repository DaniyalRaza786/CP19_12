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
from datetime import date
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def hello():
    if request.method=='POST':
        name=request.form['feed']
        images=request.files['picture']
        
        
        if name != "":
             db.child("new_post").push({"post":name})
             new_post=db.child("new_post").get()
             new=new_post.val()
             return render_template('Home.html',post=new.values())
        if images != "":
             storage.child("image/new2.jpg").put(images)
             link=storage.child("image/new2.jpg").get_url(None)
             return render_template('Home.html',l=link)
    new_post=db.child("new_post").get()
    new=new_post.val()
    link=storage.child("image/new2.jpg").get_url(None)
    return render_template('Home.html',post=new.values(),l=link)
@app.route('/comment', methods=['GET','POST'])
def comments():
    if request.method=='POST':
        comment=request.form['comment']
        if comment != "":
<<<<<<< HEAD
            today = date.today()
            db.child("comment").push({"new_comment":comment,"date":today})
            new_comment=db.child("comment").get()
            new_comment_post=new_comment.val()
            return render_template('Home.html',new_comment_post=new_comment_post.values())
    new_post=db.child("new_post").get()
    new=new_post.val()
    link=storage.child("image/new2.jpg").get_url(None)
    new_comment=db.child("comment").get()
    new_comment_post=new_comment.val()
    return render_template('Home.html',post=new.values(),l=link,new_comment_post=new_comment_post.values())  
=======
            
            db.child("comment").push({"new_comment":comment})
            new_comment=db.child("comment").get()
            new=new_comment.val()
            return render_template('Home.html',comment=new.values())
    new_post=db.child("new_post").get()
    new=new_post.val()
    link=storage.child("image/new2.jpg").get_url(None)
    return render_template('Home.html',post=new.values(),l=link)  
>>>>>>> 5dea821da23027f196959d08e8819293f6ca2f20
    
@app.route("/Taha")
def Taha():
    return "Hello taha!"
app.run(debug=True)