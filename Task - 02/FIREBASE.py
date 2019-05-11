import pyrebase
config = {

   "apiKey": "AIzaSyDLjSzb74WFvOZgLno5fo7klW0qTiAfRTg",
    "authDomain": "task2-dbe0c.firebaseapp.com",
    "databaseURL": "https://task2-dbe0c.firebaseio.com",
    "projectId": "task2-dbe0c",
    "storageBucket": "task2-dbe0c.appspot.com",
    "messagingSenderId": "830523653527"

}

firebase =pyrebase.initialize_app(config)
db=firebase.database()
# FOR DATA INSERT
db.child("names").push({"name":"DaniyaL RAZA"})
#FOR UPDATE
db.child("names").update({"name":"DaniyaL"})
#FOR REMOVE DATA
db.child("names").remove({"name":"DaniyaL RAZA"})