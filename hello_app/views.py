from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello")
def hello_there():

	name = request.args.get("name")
	if not name:
		return redirect(url_for("home"))
	
	return render_template(
		"hello_there.html",
		name=name.capitalize(),
		date=datetime.now()
	)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
