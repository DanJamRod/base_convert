# export FLASK_APP=app.py && python3 -m flask run
from base import base as base
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "SuperSecretKey" # Secret Key required for session["start"] to store info

@app.route('/',methods=['POST','GET'])
def index():
    """ Index/home page. Choose whether conversion or 
    """
    if request.method =='POST':
        session["request_type"] = request.form["request_type"]
        if session["request_type"] == "convert":
            return redirect(url_for("convert"))
        if session["request_type"] == "operation":
            return redirect(url_for("operation"))
    else:
        return render_template("index.html")

@app.route("/convert")
def convert():
    """ Convert between bases
    """
    try:
        text = "Placeholder"
        return render_template("convert.html")
    except:
        return render_template('error.html')

@app.route("/operation")
def operation():
    """ Perform an operation in any base
    """
    try:
        text = "Placeholder"
        return render_template("convert.html")
    except:
        return render_template('error.html')