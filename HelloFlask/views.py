from datetime import datetime
from re import match

from flask import Flask, render_template

from HelloFlask import app


@app.route('/')
def home():
    return render_template("home.html", title="Home")

@app.route('/about')
def about():
    return render_template("about.html", title="About us")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact us")

@app.route('/hello/<name>')
def hello_there(name):
    return render_template(
        "hello_there.html",
        title ='Hello, Flask',
        name = clean_name(name),
        date = datetime.now()
    )

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

def clean_name(name):
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    return clean_name
