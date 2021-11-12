# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask, redirect, url_for  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from database import db
from models import Post as Post
from models import User as User
from datetime import date

app = Flask(__name__)  # create an app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class_forum_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()  # run under the app context


# code for index function
# list posts
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if "view" in request.form.keys():
            request.form['view']
            # return redirect(url_for('note'), post_id=request.form['id'])
        elif "edit" in request.form.keys():
            return redirect(url_for('edit', post_id=request.form['id']))
    # get all posts from database
    my_posts = db.session.query(Post).all()
    return render_template('index.html', posts=my_posts)


# create a new post
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


# edit post
@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def edit(post_id):
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = db.session.query(Post).filter_by(id=post_id).one()
        post.title = title
        post.text = text
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        my_post = db.session.query(Post).filter_by(id=post_id).one()
        return render_template('edit.html', post=my_post)


# Delete post
@app.route('/delete/<post_id>', methods=['POST'])
def delete_post(post_id):
    post = db.session.query(Post).filter_by(id=post_id).one()
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('index'))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
