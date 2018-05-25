from flask import Flask
from flask import render_template
from HelloFlask import app

@app.route('/')
def home():
    return render_template("home.html", title = "Home")

@app.route('/about')
def about():
        return render_template("about.html", title = "About us")

@app.route('/contact')
def contact():
        return render_template("contact.html", title = "Contact us")

@app.route('/hello/<name>')
def hello_there(name):
    from datetime import datetime
    now = datetime.now()

    return render_template(
        "hello_there.html",
        title ='Hello, Flask',
        message = "Hello there, " + name + "!",
        date = now.strftime("%A, %d %B, %Y at %X")
    )

@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')