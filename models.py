import datetime
from database import db


class Post(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(500))
    date = db.Column("date", db.String(50))
    imagename = db.Column("imagename", db.String(50))
    imageid = db.Column("imageid", db.Integer)
    imagetype = db.Column("imagetype", db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    comments = db.relationship("Comment", backref="post", cascade="all, delete-orphan", lazy=True)
    is_pinned = db.Column(db.Boolean, default=False)

    def __init__(self, title, text, date, imagename, imageid, imagetype, user_id):
        self.title = title
        self.text = text
        self.date = date
        self.imagename = imagename
        self.imageid = imageid
        self.imagetype = imagetype
        self.user_id = user_id


class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    posts = db.relationship("Post", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.VARCHAR, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, content, post_id, user_id):
        self.date_posted = datetime.date.today()
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
