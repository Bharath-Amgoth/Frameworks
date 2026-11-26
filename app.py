from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    first_name="Bharath"
    last_name="Amgoth"
    course="Flask"
    city="mahabubabad"
    age=23
    price=1000
    return render_template("index.html",first_name=first_name,last_name=last_name,
                           course=course,city=city,age=age,price=price)
if __name__ == ("__main__"):
    app.run(debug=True)