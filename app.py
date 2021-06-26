import json
from werkzeug.utils import secure_filename
import os
from flask import Flask , render_template , request , redirect , url_for , flash , session
from markupsafe import escape
import string,random , datetime , math , time
from flask_sqlalchemy import SQLAlchemy


with open('config.json','r') as c:
    params = json.load(c)["params"]

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', }
app = Flask(__name__)
pool_size=20
max_overflow=0
# if params['local_server']:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
app.config['SECRET_KEY'] = "sending messages"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    ID_Number = db.Column(db.String(10),db.ForeignKey('user_credential.ID_Number'),primary_key=True)
    Name = db.Column(db.String(150))
    Bio = db.Column(db.String(1000))
    Country = db.Column(db.String(150))
    Phone_no = db.Column(db.String(15))
    Email = db.Column(db.String(150))
    Profile_img = db.Column(db.String(100))
    Friends = db.relationship('Followed', backref='profile_info',lazy='dynamic')


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
    Reading = db.relationship('Reading_list',lazy ='dynamic')
    
class Reading_list(db.Model):
    __tablename__ = 'reading_list'
    id = db.Column(db.Integer, primary_key=True)
    News_ID = db.Column(db.String(150),db.ForeignKey('news.News_ID'))
    User_ID = db.Column(db.String(100))

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


@app.route('/')
async def home():
    tic = time.perf_counter()
    No_post =  params['no_of_post']
    Article = News.query.all()
    Article.reverse()
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
    toc = time.perf_counter()
    print(toc - tic)
    if 'id_no' in session :
        return render_template('home.html',ID_Number = escape(session['id_no']),Article=Article,prev=prev,old=old,num=page,last=last)
    
    return render_template('home.html',Article=Article,prev=prev,old=old,num=page,last=last)


@app.route('/repoter',methods=['GET', 'POST'])
async def login_register():
    tic = time.perf_counter()
    if request.method == 'POST':
        if request.form['tab']== '1':  
            id_no = request.form['id_no']
            username = request.form['username']
            password = request.form['password']
            if User_credential.query.filter_by(ID_Number = id_no).first():
                if User_credential.query.filter_by(Username = username , Password = password).first():
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
    toc = time.perf_counter()
    print(toc - tic)
    return render_template('login_register.html')

@app.route('/profile/<user_id>', methods = ['GET','POST'])
@app.route('/profile', methods = ['GET','POST'])
async def profile(user_id=None):
    tic = time.perf_counter()
    if 'id_no' in session :
        id_no =str(escape(session['id_no']))
        otheruser = False
        if user_id: 
            if id_no == user_id :
              otheruser = False
            else:
              otheruser = True
              id_no = user_id

        User = Profile_info.query.filter_by(ID_Number = id_no).first()
        followed = Followed.query.filter_by(User_ID = id_no)
        follower = Followed.query.filter_by(Followed_ID = id_no)
        article = News.query.filter_by(User_ID = id_no).all()
        reading = Reading_list.query.filter_by(User_ID = id_no).all()
        alluser = Profile_info.query.all()
        allnews = News.query.all()
        if request.method == 'POST':

          if request.form['fol'] == '2':  
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
          if request.form['fol']== '1':
            follow = request.form['follow']
            id = str(escape(session['id_no']))
            print(request.form['op'])
            if request.form['op'] == 'Follow':
              if Followed.query.filter_by(User_ID = id,Followed_ID = follow).first():
                  pass
              elif follow:
                  Create = Followed(User_ID = id, Followed_ID = follow)
                  db.session.add(Create)
                  db.session.commit()

            if request.form['op'] == 'Unfollow' :
              if Followed.query.filter_by(User_ID = id,Followed_ID = follow).first():
                  Followed.query.filter_by(User_ID = id,Followed_ID = follow).delete()
                  db.session.commit()
              else:
                  pass
        toc = time.perf_counter()
        print(toc - tic)
        return render_template('profile.html',User = User,Article = article,otheruser=otheruser,Follower = follower,Followed=followed,Reading = reading,Alluser = alluser,Allnews = allnews)
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
    tic = time.perf_counter()
    if 'id_no' in session:
        if request.method == 'POST':
            while True :
               news_id =''.join(random.choices(string.ascii_uppercase + string.digits,k=30))
               News_ID = News.query.filter_by(News_ID = news_id).first()
               if News_ID:
                   continue
               else :
                   break
            id_no = str(escape(session['id_no']))           
            title = request.form['title']
            thumb = request.form['thumbnail']
            locat = request.form['location']
            tag = request.form['tag']
            descrip = request.form['discrip']
            date1 = datetime.date.today()
            create = News(User_ID = id_no,News_ID = news_id,Thumbnail = thumb,Location = locat,Tag=tag,Description = descrip,Title = title,Date =date1)
            db.session.add(create)
            db.session.commit()
            toc = time.perf_counter()
            print(toc - tic)
            return redirect(url_for('profile'))
        toc = time.perf_counter()
        print(toc - tic)
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
          id = str(escape(session['id_no']))
          if request.method == 'POST':
            read = request.form['read']
            if Reading_list.query.filter_by(User_ID = id,News_ID = read).first():
                pass
            elif read:
                Create = Reading_list(User_ID = id, News_ID = read)
                db.session.add(Create)
                db.session.commit()
        try: 
           No_post = params['no_of_post']           
           page = request.args.get('page')
           if (not str(page).isnumeric()):
                 page = 1
           page = int(page)
           Article = News.query.filter_by(News_ID = article).first()
           if Article:
              if 'id_no' in session: 
                if Article.User_ID == id:
                  owner = True
              else:
                  unknow = False
              return render_template('news.html',Article= Article,Owner = owner,Unknow = unknow)
           Article = News.query.filter_by(Tag = article).all()
           if Article:
              Article.reverse()
              last = math.ceil(len(Article)/int(No_post))
              Article = Article[(page-1) * int(No_post) : (page-1) * int(No_post) +int(No_post) ]
              if page == 1:
                  prev = "#"
                  old = "/news/"+ article +"/?page="+ str(page+1)
              if page == last :
                 prev = "/news/"+ article +"/?page="+ str(page-1)
                 old = "#"
              else:
                 prev = "/news/"+ article +"/?page="+ str(page-1)
                 old = "/news/"+ article +"/?page="+ str(page+1)
              return render_template('newspage.html',Article= Article,Owner=owner,prev=prev,old=old,num=page,last=last)
           else:
                flash('NEWS is NOT Available Sorry !!')
                return redirect(url_for('home'))

        except Exception as e:
            flash('NEWS is NOT Available Sorry !!')
            return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))


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
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        Create = Contact(Name = name , Email = email , Message = message)
        db.session.add(Create)
        db.session.commit()

    return render_template('contact.html')

@app.before_request
async def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=60)

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
        return 'Working in Progress'
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
   db.create_all()
   app.run(debug=False)
