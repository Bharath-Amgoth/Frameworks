from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    courses=["Flask",
             "Python",
             "React",
             "Django"]
    #dict variables
    student={
        "Name":"Bharath Amgoth",
        "Course":"Python Fullstack",
        "Age":23,
        "City":"Mahabubabad"
    }
    return render_template("index.html",courses=courses,student=student)
if __name__==("__main__"):
    app.run(debug=True)