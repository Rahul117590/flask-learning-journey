from flask import Flask,render_template

app=Flask(__name__)
# this is used to connect the app with the browser


@app.route("/")
def home():
    return render_template('home.html')



# for run the file 
if __name__== '__main__':
    app.run(debug=True)