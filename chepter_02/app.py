from flask import Flask,render_template,request

app=Flask(__name__)
# this is used to connect the app with the browser


@app.route("/")
def login():
    return render_template('login.html')

@app.route("/submit",methods=['POST'])
def submit():
    username=request.form.get('username')#read the user name
    password=request.form.get('password')# read the password

    if username=='rahul' and password=='123':
        return render_template('welcome.html', name=username)
    
    else:
        return 'invalid credentials'


# for run the file 
if __name__== '__main__':
    app.run(debug=True)