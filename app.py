# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for 

app = Flask(__name__)     # create an app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        # TODO Update database

        return redirect(url_for('index'))
    else:
        return render_template('post.html')

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)