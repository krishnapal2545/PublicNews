from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime, json

SQLALCHEMY_ENGINE_OPTIONS = {
    "max_overflow": 10000,
    "pool_pre_ping": True,
    "pool_recycle": 60 * 60,
    "pool_size": 30000,
}
UPLOAD_FOLDER = 'static/'
with open('config.json','r') as c:
    params = json.load(c)["params"]

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    # if params['local_server']:
    #     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
    # else:
    #     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']  
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    app.config['SECRET_KEY'] = "sending messages"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_ENGINE_OPTIONS']= SQLALCHEMY_ENGINE_OPTIONS
    app.config['MAX_CONTENT_LENGTH'] = 16* 1024 *1024
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return app

class User_credential(db.Model):
    __tablename__ = 'user_credential'
    ID_Number = db.Column(db.String(10) ,primary_key = True)
    Phone_Number = db.Column(db.String(15))
    Username = db.Column(db.String(50))
    Password = db.Column(db.String(50))

class Profile_info(db.Model):
    __tablename__ = 'profile_info'
    id = db.Column(db.Integer, primary_key=True)
    ID_Number = db.Column(db.String(10),primary_key=True)
    Name = db.Column(db.String(150))
    Bio = db.Column(db.String(1000))
    Country = db.Column(db.String(150))
    Phone_no = db.Column(db.String(15))
    Email = db.Column(db.String(150))
    Profile_img = db.Column(db.String(100))
    Friends = db.relationship('Followed', backref='profile_info',lazy='dynamic')
    Reading = db.relationship('Reading_list',backref='profile_info',lazy ='dynamic')

class News(db.Model):
    __tablename__ = 'news'
    Srno = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.String(10),primary_key=True)
    News_ID = db.Column(db.String(150),primary_key=True)
    Thumbnail = db.Column(db.String(2048))
    Title = db.Column(db.String(100))
    Date = db.Column(db.String(100))
    Description = db.Column(db.String())
    Location = db.Column(db.String(10000))
    Tag = db.Column(db.String(100))
    Comment = db.relationship('Comments',backref='news',lazy = 'dynamic')
    
class Reading_list(db.Model):
    __tablename__ = 'reading_list'
    id = db.Column(db.Integer, primary_key=True)
    News_ID = db.Column(db.String(150))
    User_ID = db.Column(db.String(100),db.ForeignKey('profile_info.ID_Number'))

class Followed(db.Model):
    __tablename__ = 'followed'
    id = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.String(100),db.ForeignKey('profile_info.ID_Number'))
    Followed_ID = db.Column(db.String(100))

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Message = db.Column(db.String())

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    News_ID = db.Column(db.String(100), db.ForeignKey('news.News_ID'))
    User_ID = db.Column(db.String(100))
    Comment = db.Column(db.String())
    Date = db.Column(db.DateTime(),default=datetime.datetime.utcnow)