# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask, session, redirect, url_for  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from database import db
from models import Post as Post
from models import User as User
from models import Comment as Comment
from datetime import date
from werkzeug.utils import secure_filename
from sqlalchemy.sql import func
from forms import CommentForm

app = Flask(__name__)  # create an app


UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg'}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class_forum_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(imageid) + "." + file_name.rsplit('.', 1)[1].lower()))

        today = date.today()

        today = today.strftime("%m-%d-%Y")

        new_post_object = Post(title, text, today, file_name, imageid, image_type)

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
    if (post.imageid != -1):
        os.remove("./static/images/" + str(post.imageid) + "." + post.imagetype)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('index'))


# create user log of posts
@app.route('/post_catalog.html')
def user_log():
    return render_template('post_catalog.html')


# register a user
@app.route('/register')
def register():
    return render_template('register.html')


# login feature
@app.route('/login')
def login():
    return render_template('login.html')


# logout feature
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# filter posts
# I want to filter responses by date posted, title, and the user who posted it
@app.route('/filter')
def filter_post():
    # retrieve posts from database
    return redirect(url_for('index'))


# Create a Comment
@app.route('/notes/<note_id>/comment', methods=['POST'])
def new_comment(note_id):
    if session.get('user'):
        comment_form = CommentForm()
        # validate_on_submit only validates using POST
        if comment_form.validate_on_submit():
            # get comment data
            comment_text = request.form['comment']
            new_record = Comment(comment_text, int(note_id), session['user_id'])
            db.session.add(new_record)
            db.session.commit()

        return redirect(url_for('get_note', note_id=note_id))

    else:
        return redirect(url_for('index'))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
