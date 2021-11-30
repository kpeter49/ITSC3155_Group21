# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask, redirect, url_for  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from database import db
from models import Post as Post
from models import User as User
from datetime import date
from forms import RegisterForm, LoginForm
from flask import session
import bcrypt


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
            my_post = db.session.query(Post).filter_by(id=request.form['id']).one()
            return render_template('note.html', post_id=request.form['id'], note=my_post)
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


# create user log of posts
@app.route('/post_catalog.html')
def user_log():
    return render_template('post_catalog.html')


# register a user
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():

        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())

        username = request.form['username']

        new_user = User(username, request.form['email'], h_password)

        db.session.add(new_user)
        db.session.commit()

        session['user'] = username
        session['user_id'] = new_user.id  # access id value from user model of this newly added user

        return redirect(url_for('index'))


    return render_template('register.html', form=form)


# login feature
@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():

        the_user = db.session.query(User).filter_by(email=request.form['email']).one()

        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):

            session['user'] = the_user.username
            session['user_id'] = the_user.id

            return redirect(url_for('index'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)



# logout feature
@app.route('/logout')
def logout():

    if session.get('user'):
        session.clear()

    return redirect(url_for('index'))


@app.route('/image')
def attach_image():
    return redirect(url_for('index'))


# filter posts
# I want to filter responses by date posted, title, and the user who posted it
@app.route('/filter')
def filter_post():
    # retrieve posts from database
    return redirect(url_for('index'))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
