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
    """ Convert between bases query
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
    session["converted_num"] = base(str(session["convert_num"]), int(session["base_from"]), int(session["base_to"]))
    try:
        return render_template("convert_result.html")
    except:
        return render_template('error.html')

@app.route('/operation',methods=['POST','GET'])
def operation():
    """ Operations on numbers with different bases query 
    """
    if request.method =='POST':
        session["num_1"] = request.form["num_1"]
        session["base_1"] = request.form["base_1"]
        session["operation"] = request.form["operation"]
        session["num_2"] = request.form["num_2"]
        session["base_2"] = request.form["base_2"]
        session["base_3"] = request.form["base_3"]
        return redirect(url_for("operation_result"))
    else:
        return render_template("operation.html")


@app.route('/operation_result')
def operation_result():
    """ Operations on numbers with different bases result
    """
    try:
        if session["operation"] == "^":
            session["operation_result"] = base(int(base(str(session["num_1"]), int(session["base_1"]), 10)) ** int(base(str(session["num_2"]), int(session["base_2"]), 10)), 10, int(session["base_3"]))
        if session["operation"] == "*":
            session["operation_result"] = base(int(base(str(session["num_1"]), int(session["base_1"]), 10)) * int(base(str(session["num_2"]), int(session["base_2"]), 10)), 10, int(session["base_3"]))
        if session["operation"] == "/":
            session["operation_result"] = f'{base(int(base(str(session["num_1"]), int(session["base_1"]), 10)) // int(base(str(session["num_2"]), int(session["base_2"]), 10)), 10, int(session["base_3"]))}r{base(int(base(str(session["num_1"]), int(session["base_1"]), 10)) % int(base(str(session["num_2"]), int(session["base_2"]), 10)), 10, int(session["base_3"]))}'
        if session["operation"] == "+":
            session["operation_result"] = base(int(base(str(session["num_1"]), int(session["base_1"]), 10)) + int(base(str(session["num_2"]), int(session["base_2"]), 10)), 10, int(session["base_3"]))
        if session["operation"] == "-":
            session["operation_result"] = base(int(base(str(session["num_1"]), int(session["base_1"]), 10)) - int(base(str(session["num_2"]), int(session["base_2"]), 10)), 10, int(session["base_3"]))                                            
        return render_template("operation_result.html")
    except:
        return render_template('error.html')