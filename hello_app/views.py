import datetime

import flask

from hello_app import app


@app.route("/")
def home():
    return flask.render_template("home.html")


@app.route("/about")
def about():
    return flask.render_template("about.html")


@app.route("/contact")
def contact():
    return flask.render_template("contact.html")


@app.route("/hello/<name>")
def hello_there(name):
    date = datetime.datetime.now()
    return flask.render_template("hello_there.html", name=name, date=date)


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
