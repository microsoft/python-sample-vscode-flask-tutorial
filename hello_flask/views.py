from datetime import datetime
from flask import Flask, render_template
from hello_flask import app

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
        title='Hello, Flask',
        name=name,
        date=datetime.now()
    )

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')
