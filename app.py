# imports
import os  # os is used to get environment variables IP & PORT
from sqlite3 import Date

from flask import Flask, session, redirect, url_for  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from database import db
from models import Post as Post
from models import User as User
from models import Comment as Comment
from datetime import date
from forms import RegisterForm, LoginForm
from flask import session
import bcrypt

from werkzeug.utils import secure_filename
from sqlalchemy.sql import func
from forms import CommentForm

app = Flask(__name__)  # create an app

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg'}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class_forum_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'SE3155'
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()  # run under the app context


# code for index function
# list posts
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if session.get('user'):
        if request.method == 'POST':
            if "view" in request.form.keys():
                request.form['view']
                my_post = db.session.query(Post).filter_by(id=request.form['id']).one()
                # create a comment form object
                form = CommentForm()

                return render_template('note.html', post_id=request.form['id'], post=my_post, form=form, user=session['user'])
            elif "edit" in request.form.keys():
                return redirect(url_for('edit', post_id=request.form['id']))
        # get all posts from database
        my_posts = db.session.query(Post).filter_by(user_id=session['user_id']).all()
        return render_template('index.html', posts=my_posts, user=session['user'])
    else:
        return redirect(url_for('login'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# create a new post
@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        imageid = -1
        image_type = ""

        file = None
        file_name = ""
        if 'file' in request.files:
            file = request.files['file']
            file_name = file.filename

        # check if there is no file specified
        if file.filename == '':
            file = None

        if file and allowed_file(file_name):
            file_name = secure_filename(file.filename)
            image_type = file_name.rsplit('.', 1)[1].lower()
            imageid = db.session.query(func.max(Post.imageid)).scalar()

            if imageid != None:
                imageid += 1
            else:
                imageid = 0
            file.save(
                os.path.join(app.config['UPLOAD_FOLDER'], str(imageid) + "." + file_name.rsplit('.', 1)[1].lower()))

        today = date.today()

        today = today.strftime("%m-%d-%Y")

        new_post_object = Post(title, text, today, file_name, imageid, image_type, session['user_id'])

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

    if post.imageid != -1:
        os.remove("./static/images/" + str(post.imageid) + "." + post.imagetype)
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


# filter posts
# I want to filter responses by date posted and the user who posted it
# search for posts
@app.route('/filter', methods=['GET'])
def filter_post(search):
    search_results = []
    search_exp = search.data['search_results']
    # get all search results and put them into list
    if search_exp:
        # if we filter by user
        if search.data['select'] == 'User':
            enquiry = db.session.query(Post, User).filter
            (User.id == Post.user_id).filter(User.name.contains(search_exp))
            search_results = [item[0] for item in enquiry.all()]
        # search by post title
        elif search.data['select'] == 'Post':
            enquiry = db.session.query(Post).filter(Post.title.contains(search_exp))
            search_results = enquiry.all()
        # search by date posted
        elif search.data['select'] == 'Date':
            enquiry = db.session.query(Date).filter(Date.strftime('%m-%d-%Y'))
            search_results = enquiry.all()
        else:
            enquiry = db.session.query(Post)
            search_results = enquiry.all()
    else:
        enquiry = db.session.query(Post)
        search_results = enquiry.all()

    # if no search results were found
    # return to the main page
    if not search_results:
        return redirect(url_for('/index'))
    else:
        # db_table = Results(results)
        # db_table.border = True
        return render_template('search_results.html')


# Create a Comment
@app.route('/notes/<post_id>/comment', methods=['POST'])
def new_comment(post_id):
    if session.get('user'):
        comment_form = CommentForm()
        # validate_on_submit only validates using POST
        if comment_form.validate_on_submit():
            # get comment data
            comment_text = request.form['comment']
            new_record = Comment(comment_text, int(post_id), session['user_id'])
            db.session.add(new_record)
            db.session.commit()

        my_post = db.session.query(Post).filter_by(id=post_id).one()
        return render_template('note.html', post_id=post_id, post=my_post, form=comment_form, user=session['user'])

    else:
        return redirect(url_for('index'))


# Pin Post
@app.route('/pin/<post_id>', methods=['POST'])
def pin_post(post_id):
    post = db.session.query(Post).filter_by(id=post_id).one()
    if not post.is_pinned:
        post.is_pinned = True
    elif post.is_pinned:
        post.is_pinned = False
    db.session.commit()

    return redirect(url_for('index'))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
