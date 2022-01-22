from newsapi import NewsApiClient
from sqlalchemy.orm import backref
from werkzeug.utils import secure_filename
from flask import Flask , render_template , request , redirect , url_for , flash , session
from markupsafe import escape
import string,random , datetime , math , json , os
from flask_sqlalchemy import SQLAlchemy


with open('config.json','r') as c:
    params = json.load(c)["params"]

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', }
app = Flask(__name__)

newsapi = NewsApiClient(api_key='b92898cd55d748f0a04175e18f3bcb82')

SQLALCHEMY_ENGINE_OPTIONS = {
    "max_overflow": 10000,
    "pool_pre_ping": True,
    "pool_recycle": 60 * 60,
    "pool_size": 30000,
}

if params['local_server']:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
# app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
app.config['SECRET_KEY'] = "sending messages"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_ENGINE_OPTIONS']= SQLALCHEMY_ENGINE_OPTIONS
app.config['MAX_CONTENT_LENGTH'] = 16* 1024 *1024
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

# @celery.task(bind=True)
def getid():
    id_no = escape(session['id_no'])
    User = User_credential.query.filter_by(ID_Number = str(id_no)).first()
    return User.ID_Number

async def allnews():
    Article = News.query.all()
    Article.reverse()
    return Article

@app.before_request
async def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=60)

@app.route('/topnews/<type>')
@app.route('/topnews')
async def topnews(type=None):
   try:
    if type == 'Worlds':
        news = newsapi.get_everything(q='World')
    elif type == 'Technology':
        news = newsapi.get_everything(q='Technology')
    elif type == 'Culture':
        news = newsapi.get_everything(q='Culture')
    elif type == 'Business':
        news = newsapi.get_everything(q='Business')
    elif type == 'Politics':
        news = newsapi.get_everything(q='Politics')
    elif type == 'Science':
        news = newsapi.get_everything(q='Science')
    elif type == 'Health':
        news = newsapi.get_everything(q='Health')
    elif type == 'Sports':
        news = newsapi.get_everything(q='Sports')
    elif type == 'Travel':
        news = newsapi.get_everything(q='Travel')
    else:
        news = newsapi.get_top_headlines(country="in")
    return render_template('topnews.html',Article = news['articles'])
   except Exception as e:
       print(f"Exception is :->{e}")
       flash(' No Internet Connection ')
       return redirect('/')


@app.route('/')
async def home():
    No_post =  params['no_of_post']
    Article = await allnews()
    last = math.ceil( len(Article)/int(No_post))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    Article = Article[(page-1) * int(No_post) : (page-1) * int(No_post) +int(No_post) ]
    if page == 1:
        prev = "#"
        old = "/?page="+ str(page+1)
    elif page == last :
        prev = "/?page="+ str(page-1)
        old = "#"
    else:
        prev = "/?page="+ str(page-1)
        old = "/?page="+ str(page+1)
    if 'id_no' in session :
        return render_template('home.html',ID_Number = escape(session['id_no']),Article=Article,prev=prev,old=old,num=page,last=last)
    
    return render_template('home.html',Article=Article,prev=prev,old=old,num=page,last=last)


@app.route('/repoter',methods=['GET', 'POST'])
async def login_register():
    if request.method == 'POST':
        if request.form['tab']== '1':  
            id_no = request.form['id_no']
            username = request.form['username']
            password = request.form['password']
            if  User_credential.query.filter_by(ID_Number = id_no).first():
                if  User_credential.query.filter_by(Username = username , Password = password).first():
                    session['id_no'] = id_no
                    return redirect(url_for('home'))
                else:
                    flash(' Invalide UserName or Password ')
            else :
                flash(' Invalide ID NUMBER ')

        elif request.form['tab']=='2':
            while True :
               id_no =''.join(random.choices(string.ascii_uppercase + string.digits,k=10))
               ID_No = User_credential.query.filter_by(ID_Number = id_no).first()
               if ID_No :
                   continue
               else :
                   break
            phone_no = request.form['phone_no']
            username = request.form['username']
            password = request.form['password']
          
            create = User_credential(ID_Number= id_no,Phone_Number= phone_no,Username= username,Password= password)
            db.session.add(create)
            db.session.commit()
            create = Profile_info(ID_Number= id_no)
            db.session.add(create)
            db.session.commit()
            flash(f'Your Registration is done and Your ID Number is {id_no}')
    return render_template('login_register.html')

async def profinfo(id_no):
    user = Profile_info.query.filter_by(ID_Number = id_no).first()
    return user

async def profnews(id_no):
    article = News.query.filter_by(User_ID = id_no).all()
    return article

@app.route('/profile', methods = ['GET','POST'])
async def profile():
    if 'id_no' in session :
        id_no =str(escape(session['id_no']))
        if request.method == 'POST':  
            name = request.form['name']
            country = request.form['country']
            phone_no = request.form['phone_no']
            email = request.form['email']
            bio = request.form['bio']
            f = request.files['profile']
            if f :
              filename = secure_filename(f.filename)
              f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            User = Profile_info.query.filter_by(ID_Number = id_no).first()
            if name :  User.Name = name
            if country :  User.Country = country
            if phone_no :  User.Phone_no = phone_no
            if email :  User.Email = email
            if bio :  User.Bio = bio
            if f : User.Profile_img = filename
            db.session.commit()
        User = await profinfo(id_no)
        article = await profnews(id_no)
        article.reverse()
        return render_template('profile.html',User = User,Article = article,otheruser=False)
    else:
        return redirect(url_for('login_register'))

@app.route('/profile/<user_id>', methods = ['GET','POST'])
async def otherprofile(user_id=None):
    if 'id_no' in session :
        id_no =str(escape(session['id_no']))
        otheruser = Profile_info.query.filter_by(ID_Number = id_no).first()
        if user_id: 
            if id_no == user_id :
              return redirect(url_for('profile'))
            else:
              id_no = user_id
        User = Profile_info.query.filter_by(ID_Number = id_no).first()
        f=False
        for i in otheruser.Friends:
            if i.Followed_ID == id_no:
                f=True
                break
            else:
                f=False
        follow = request.args.get('user')
        friend = request.args.get('id')
        id = str(escape(session['id_no']))
        if follow == 'Follow':
            print('hii')
            if Followed.query.filter_by(User_ID = id,Followed_ID = friend).first():
                pass
            else:
                Create = Followed(User_ID = id, Followed_ID = friend)
                db.session.add(Create)
                db.session.commit()
            return redirect(f'/profile/{id_no}')
        if follow == 'Unfollow' :
            print('hii')
            if Followed.query.filter_by(User_ID = id,Followed_ID = friend).first():
                print('hii2')
                Followed.query.filter_by(User_ID = id,Followed_ID = friend).delete()
                db.session.commit()
            else:
                pass
            return redirect(f'/profile/{id_no}')
        return render_template('profile.html',User = User,otheruser=True,follow=f)
    else:
        return redirect(url_for('login_register'))

@app.route('/usernews/<id>')
@app.route('/usernews')
async def usernews(id=None):
    if 'id_no' in session :
        if id:
          article =  News.query.filter_by(User_ID = id).all()
          article.reverse()
          User = Profile_info.query.filter_by(ID_Number = id).first()
          return render_template('usernews.html',Article=article,otheruser=True,User=User)
        else:
          id_no = getid()
          article =  News.query.filter_by(User_ID = id_no).all()
          article.reverse()
          return render_template('usernews.html',Article=article)
    else:
        return redirect(url_for('login_register'))


@app.route('/readinglist')
async def read():
    if 'id_no' in session :
        id_no = getid()
        User =  Profile_info.query.filter_by(ID_Number = id_no).first()
        allnews = News.query.all()
        allnews.reverse()
        return render_template('readinglist.html',Allnews =allnews,User = User )
    else:
        return redirect(url_for('login_register'))


@app.route('/followers')
async def follower():
    if 'id_no' in session :
        id_no = getid()
        follower = Followed.query.filter_by(Followed_ID = id_no)
        alluser = Profile_info.query.all()
        return render_template('follower.html',Alluser = alluser,Follower = follower )
    else:
        return redirect(url_for('login_register'))


@app.route('/following')
async def following():
    if 'id_no' in session :
        id_no = getid()
        User = Profile_info.query.filter_by(ID_Number = id_no).first()
        alluser = Profile_info.query.all()
        return render_template('following.html',Alluser = alluser,User = User )
    else:
        return redirect(url_for('login_register'))


@app.route('/chatlist')
async def chatlist():
    if 'id_no' in session :
        id_no = getid()
        User = Profile_info.query.filter_by(ID_Number = id_no).first()
        article = News.query.filter_by(User_ID = id_no).all()
        article.reverse()
        follower = Followed.query.filter_by(Followed_ID = id_no)
        alluser = Profile_info.query.all()
        return render_template('chatlist.html',Article=article,User = User,Alluser = alluser,Follower = follower )
    else:
        return redirect(url_for('login_register'))


@app.route('/logout')
async def logout():
    if 'id_no' in session :
        session.pop('id_no', None)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_register'))


@app.route('/addnews',methods=['GET', 'POST'])
async def addnews():
    if 'id_no' in session:
        if request.method == 'POST':
            while True :
               news_id =''.join(random.choices(string.ascii_uppercase + string.digits,k=30))
               News_ID = News.query.filter_by(News_ID = news_id).first()
               if News_ID:
                   continue
               else :
                   break
            id_no = getid()          
            title = request.form['title']
            thumb = f"https://drive.google.com/uc?export=view&id={request.form['thumbnail']}"
            locat = request.form['location']
            tag = request.form['tag']
            descrip = request.form['discrip']
            date1 = datetime.date.today()
            create = News(User_ID = id_no,News_ID = news_id,Thumbnail = thumb,Location = locat,Tag=tag,Description = descrip,Title = title,Date =date1)
            db.session.add(create)
            db.session.commit()
            return redirect(url_for('profile'))
        return render_template('addnews.html')
    else:
        return redirect(url_for('home'))


@app.route('/news')
@app.route('/news/<article>',methods=['GET','POST'])
async def news(article=None):
    owner = False
    unknow = True
    if article:
        if 'id_no' in session:  
          id = getid()
          read = request.args.get('read')
          unread = request.args.get('unread')
          if read:
            if Reading_list.query.filter_by(User_ID = id,News_ID = read).first():
                pass
            else :
                Create = Reading_list(User_ID = id, News_ID = read)
                db.session.add(Create)
                db.session.commit()
            return redirect(f'/news/{read}')
          if unread:
            if Reading_list.query.filter_by(User_ID = id,News_ID = unread).first():
                Create = Reading_list.query.filter_by(User_ID = id, News_ID = unread).first()
                db.session.delete(Create)
                db.session.commit()
            else:
               pass
            return redirect(f'/news/{unread}')
        try: 
           No_post = params['no_of_post']           
           page = request.args.get('page')
           if (not str(page).isnumeric()):
                page = 1
           page = int(page)
           Article = News.query.filter_by(News_ID = article).first()
           if Article:
              feed=False
              if 'id_no' in session: 
                if Article.User_ID == id:
                  owner = True
                if Reading_list.query.filter_by(User_ID = getid(),News_ID = Article.News_ID).first():
                  feed=True
              else:
                  unknow = False
              other = News.query.filter_by(Tag= Article.Tag).all()
              other.reverse()
              alluser = Profile_info.query.all()
              return render_template('news.html',Article= Article,Owner = owner,Unknow = unknow,Relate= other,Alluser = alluser,Feed=feed)
           Article = News.query.filter_by(Tag = article).all()
           if Article:
              Article.reverse()
              last = math.ceil(len(Article)/int(No_post))
              Article = Article[(page-1) * int(No_post) : (page-1) * int(No_post) +int(No_post) ]
              if page == 1:
                  prev = "#"
                  old = "/news/"+ article +"?page="+ str(page+1)
              if page == last :
                 prev = "/news/"+ article +"?page="+ str(page-1)
                 old = "#"
              else:
                 prev = "/news/"+ article +"?page="+ str(page-1)
                 old = "/news/"+ article +"?page="+ str(page+1)
              return render_template('newspage.html',Article= Article,Owner=owner,prev=prev,old=old,num=page,last=last)
           else:
              flash('NEWS is NOT Available Sorry !!')
              return redirect(url_for('home'))
        except Exception as e:
            flash('NEWS is NOT Available Sorry !!')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/news/comment/<article>',methods=['POST'])
async def comment(article):
    if 'id_no' in session:
        id_no = str(escape(session['id_no']))
        message = request.form['comment']
        Create = Comments(User_ID=id_no,News_ID=article,Comment=message)
        db.session.add(Create)
        db.session.commit()
        return redirect(f'/news/{article}')
    else:
        return redirect('/repoter') 


@app.route('/editnews')
@app.route('/editnews/<article>', methods = ['GET','POST'])
async def editnews(article=None):
    if 'id_no' in session:
      if article:
        if request.method == 'POST':
            title = request.form['title']
            thumb = request.form['thumbnail']
            locat = request.form['location']
            tag = request.form['tag']
            descrip = request.form['discrip']
            Create = News.query.filter_by(News_ID=article).first()
            if Create:
                if title : Create.Title = title
                if thumb : Create.Thumbnail = thumb
                if locat : Create.Location = locat
                if tag : Create.Tag = tag
                if descrip : Create.Description = descrip
                db.session.commit()
            return redirect(f'/news/{article}')
        rticle = News.query.filter_by(News_ID = article).first()
        return render_template('editnews.html',Article = rticle)
    return redirect(url_for('home'))


@app.route('/contact',methods=['GET','POST'])
async def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        Create = Contact(Name = name , Email = email , Message = message)
        db.session.add(Create)
        db.session.commit()

    return render_template('contact.html')


@app.route('/news/delete/<article>')
async def deletenews(article):
    if 'id_no' in session :
        id_no = str(escape(session['id_no']))
        Article = News.query.filter_by(News_ID = article,User_ID = id_no).first()
        if Article:
            News.query.filter_by(News_ID = article).delete()
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            return redirect(url_for('login_register'))
    else:
        return redirect(url_for('login_register'))


@app.route('/chats/<friend>')
async def chats(friend):
    if 'id_no' in session:
        Friend = Profile_info.query.filter_by(ID_Number = friend).first()
        return render_template('chats.html',Friend=Friend)
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)
