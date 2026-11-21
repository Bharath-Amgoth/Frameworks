from flask import Flask
from uuid import UUID
app=Flask(__name__)


@app.route("/user/<int:id>")
def user(id):
    return f"User ID:  {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"price: {amount}"

@app.route("/employee/<string:name>/<int:id>")
def employee(name,id):
    return f"{name} your ID: {id}"

@app.route("/myfiles/<path:files>")
def myfiles(files):
    return files

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)


if __name__ == ("__main__"):
    app.run(debug=True)