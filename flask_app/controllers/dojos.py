from flask import render_template, redirect, request
from flask_app import app
from flask_app.model.dojo import Dojo 

@app.route ("/")
def index():
    x = Dojo.get_all_dojo()
    return render_template("index.html", dojos =x)

@app.route("/adddojos", methods=["POST"])
def add():
    data = {
        "name": request.form["name"]
    }
    Dojo.add(data)
    return redirect("/")

@app.route("/dojos/<int:id>")
def dojos(id):
    data ={
        "id":id
    }
    x = Dojo.all_ninja(data)
    return render_template("ninjasdojo.html", dojo=x)
