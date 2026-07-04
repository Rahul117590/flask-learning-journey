from flask import Flask


app=Flask(__name__)#this is the main page that help to build the website 

@app.route("/") # it means that it simply say that run the code that write below 
# route is use to connect the route of web page to server  @ it decorator
def home():
    return 'hello user! this is my first flask app'

@app.route("/about")
def about():
    return 'this is about page'

@app.route("/contect")
def contect():
    return 'this is contect us page'