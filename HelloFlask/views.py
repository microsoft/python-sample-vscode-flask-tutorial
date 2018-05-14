from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():        
    now = datetime.now()    

    return render_template(
        "home.html", 
        title ='Hello, Flask',
        message = "Hello, Flask!",
        date = now.strftime("%A, %d %B, %Y at %X")
    )  

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

@app.route('/about')
def about():
        return render_template("about.html", title = "About us")

@app.route('/contact')
def contact():
        return render_template("contact.html", title = "Contact us")
