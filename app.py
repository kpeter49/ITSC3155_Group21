# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for 
from database import db
from models import Post as Post
from datetime import date

app = Flask(__name__)  # create an app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class_forum_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()   # run under the app context

@app.route('/home')
def home():
    return render_template('home.html')


# code for index function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        
        today = date.today()

        today = today.strftime("%m-%d-%Y")

        new_post_object = Post(title, text, today)

        db.session.add(new_post_object)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('post.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')


@app.route('/header')
def header():
    return render_template('header.html')


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
