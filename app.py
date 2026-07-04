from flask import Flask,request



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


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        return 'you send the data!'
    else:
        return 'you are only viewing the form '

# get- if only take the information (to get the data),(no sent the information) ex - only visit some of the website
# post- it give some data and then take information  (to post the data),(sent the infomation), ex-loging in some website

