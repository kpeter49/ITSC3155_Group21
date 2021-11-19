from database import db

class Post(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(500))
    date = db.Column("date", db.String(50))
    imagename = db.Column("imagename", db.String(50))
    imageid = db.Column("imageid", db.Integer)
    imagetype = db.Column("imagetype", db.String(10))

    def __init__(self, title, text, date, imagename, imageid, imagetype):
        self.title = title
        self.text = text
        self.date = date
        self.imagename = imagename
        self.imageid = imageid
        self.imagetype = imagetype

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email