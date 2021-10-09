from flask import render_template, redirect, request
from flask_app import app
from flask_app.model import ninja, dojo

@app.route("/ninjas")
def create_ninja():
    x = dojo.Dojo.get_all_dojo()
    return render_template("ninjas.html", dojos=x)

@app.route("/createninja", methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"], 
        "age": request.form["age"], 
        "dojo_id": request.form["dojo_id"]
    }
    ninja.Ninja.create(data)
    return redirect("/")









