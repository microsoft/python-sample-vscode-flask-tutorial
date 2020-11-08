from flask import Flask  # Import the Flask class
app = Flask(__name__)    

@app.route('/')
def greet():
    print("Hello World")
