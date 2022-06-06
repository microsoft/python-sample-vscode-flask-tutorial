from datetime import datetime
from flask import Flask, render_template
from . import app

import sys
sys.stdout = open("D:/home/LogFiles/app.log', "w")
print("test")

@app.route("/")
def home():
    print("Returned index page.")
    return render_template("home.html")

@app.route("/about/")
def about():
    print("Returned about page.")
    return render_template("about.html")

@app.route("/contact/")
def contact():
    print("Returned contact page.")
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
