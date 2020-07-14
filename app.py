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

@app.route('/convert',methods=['POST','GET'])
def convert():
    """ Convert between bases 
    """
    if request.method =='POST':
        session["convert_num"] = request.form["convert_num"]
        session["base_from"] = request.form["base_from"]
        session["base_to"] = request.form["base_to"]
        return redirect(url_for("convert_result"))
    else:
        return render_template("convert.html")


@app.route('/convert_result')
def convert_result():
    """ Convert between bases result
    """
    session["converted_num"] = base(int(session["convert_num"]), int(session["base_from"]), int(session["base_to"]))
    try:
        return render_template("convert_result.html")
    except:
        return render_template('error.html')

@app.route('/operation')
def operation():
    """ Perform an operation in any base
    """
    try:
        text = "Placeholder"
        return render_template("convert.html")
    except:
        return render_template('error.html')