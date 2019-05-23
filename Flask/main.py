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
        
    new_post=db.child("new_post").get()
    new=new_post.val()
    link=storage.child("image/new2.jpg").get_url(None)
    new_comment=db.child("comment").get()
    new_comment_post=new_comment.val()
    return render_template('Home.html',post=new.values(),l=link,new_comment_post1=new_comment_post.values())  
@app.route('/post', methods=['GET','POST'])
def post():
    if request.method=='POST':
        name=request.form['feed']
        
        
        if name != "":
             db.child("new_post").push(name)
             new_post=db.child("new_post").get()
             
        
        new_post=db.child("new_post").get()
        new=new_post.val()
        link=storage.child("image/new2.jpg").get_url(None)
        new_comment=db.child("comment").get()
        new_comment_post=new_comment.val()
        return render_template('Home.html',post=new.values(),l=link,new_comment_post1=new_comment_post.values())  
@app.route('/comment', methods=['GET','POST'])
def comments():
    if request.method=='POST':
        comment=request.form['comment']
        if comment != "":
            
            db.child("comment").push(comment)
              
        new_post=db.child("new_post").get()
        new=new_post.val()
        link=storage.child("image/new2.jpg").get_url(None)
        new_comment=db.child("comment").get()
        new_comment_post=new_comment.val()
        return render_template('Home.html',post=new.values(),l=link,new_comment_post1=new_comment_post.values())  

@app.route('/image', methods=['GET','POST'])
def image():
    if request.method=='POST':
        images=request.files['picture']
        if images != "":
             storage.child("image/new2.jpg").put(images)
             
        new_post=db.child("new_post").get()
        new=new_post.val()
        link=storage.child("image/new2.jpg").get_url(None)
        new_comment=db.child("comment").get()
        new_comment_post=new_comment.val()
        return render_template('Home.html',post=new.values(),l=link,new_comment_post1=new_comment_post.values())
    
@app.route("/Taha")
def Taha():
    return "Hello taha!"

@app.route('/about', methods=['GET','POST'])
def about():
	return render_template('about.html')
app.run(debug=True)

@app.route('/event', methods=['GET','POST'])
def event():
	return render_template('event.html')
app.run(debug=True)

