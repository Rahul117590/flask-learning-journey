from flask import Flask,render_template,request

app=Flask(__name__)
#connect the data from the webserver

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/submit",methods=['POST'])
def submit():
    username=request.form.get('username')
    password=request.form.get('password')

    valid_users={
        'rahul':'123',
        'rakhi':'124',
        'gulshan':'321'
    }
    if username in valid_users and password==valid_users[username]:
        return render_template ('welcome.html',name=username)
    
    else:
        return 'invalid username and password'
    

if __name__=='__main__':
    app.run(debug=True)