# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask, redirect, url_for   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from database import db
from models import Post as Post
from models import User as User

app = Flask(__name__)     # create an app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts/delete/<post_id>', methods=['POST'])
def delete_post(post_id):
    """my_post = db.session.query(Post).filter_by(id=post_id).one()
    db.session.delete(my_post)
    db.session.commit()"""

    return render_template('home.html')  # return statement not final


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)),debug=True)
