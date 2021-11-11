# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)  # create an app


@app.route('/home')
def home():
    return render_template('home.html')


# code for index function
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/edit')
def edit():
    return render_template('edit.html')


@app.route('/header')
def header():
    return render_template('header.html')


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
