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
    comments = db.relationship("Comment", backref="note", cascade="all, delete-orphan", lazy=True)

    def __init__(self, title, text, date, imagename, imageid, imagetype):
        self.title = title
        self.text = text
        self.date = date
        self.imagename = imagename
        self.imageid = imageid
        self.imagetype = imagetype


class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))
    email = db.Column("email", db.String(100))
    # comments = db.relationship("Comment", backref="user", lazy=True)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.VARCHAR, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, content, note_id, user_id):
        self.date_posted = datetime.date.today()
        self.content = content
        self.note_id = note_id
        self.user_id = user_id
