from flask import Flask ,render_template,request


app = Flask(__name__)  # this is the name
@app.route('/')
def student_profile():
    return render_template(
        'profile.html',
        name='rahul',
        is_topper=True,
        subjects=['Maths','Science','History']

    )


if __name__=='__main__':
    app.run(debug=True)