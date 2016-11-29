import datetime
import json
import os
import psycopg2 as dbapi2
import re

from flask import Flask
from flask import redirect
from flask import render_template
from werkzeug import redirect
from flask import request
from flask.helpers import url_for, flash
from initialize_db import initialize_db_func
app = Flask(__name__)

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

#aliercccan-------------------------------------

#Login page
@app.route('/login')
def login():
    now = datetime.datetime.now()
    return render_template('log_in.html', current_time=now.ctime())


#Sign up page
@app.route('/signUp',methods = ['GET','POST'])
def signUp():

    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO USER ( USERNAME, PASSWORD) VALUES (%s,%s)"""
            print(query)

            cursor.execute(query,(username, password))
            connection.commit()

        return redirect(url_for('signUp'))
    else:
         now = datetime.datetime.now()
         return render_template('signUp.html')

#--------------- end of aliercccan ---------

#Start of Ahmet Caglar Bayatli's space

@app.route('/')
@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/home')
def home_page():
    posts = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT PostForView.ID, PostForView.FID, PostForView.POSTID FROM PostForView"""

        cursor.execute(query)

        for post in cursor:
            posts.append(post)

        connection.commit()

    return render_template('main.html', posts=posts)

@app.route('/add_post', methods = ['GET','POST'])
def add_post():
    posts = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT PostForView.ID, PostForView.FID, PostForView.POSTID FROM PostForView"""

        cursor.execute(query)

        for post in cursor:
            posts.append(post)

        connection.commit()


    if request.method =='POST':
        id = request.form['id']
        fid = request.form['fid']
        postid = request.form['postid']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO PostForView (ID, FID, POSTID ) VALUES (%s, %s, %s )"""
            cursor.execute(query, (id, fid, postid))
            connection.commit()

    return render_template('add_post.html', posts=posts)

@app.route('/delete_post', methods = ['GET','POST'])
def delete_post():
    posts = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT PostForView.ID, PostForView.FID, PostForView.POSTID FROM PostForView"""

        cursor.execute(query)

        for post in cursor:
            posts.append(post)

        connection.commit()
    if request.method =='POST':
        fid = request.form['fid']
        postid = request.form['postid']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM PostForView WHERE FID = '""" +fid + """' AND POSTID = '""" +postid + """'"""
            cursor.execute(query)
            connection.commit()

    return render_template('add_post.html', posts=posts)

@app.route('/update_post', methods = ['GET','POST'])
def update_post():
    posts = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT PostForView.ID, PostForView.FID, PostForView.POSTID FROM PostForView"""

        cursor.execute(query)

        for post in cursor:
            posts.append(post)

        connection.commit()

    if request.method =='POST':
        id = request.form['id']
        fid = request.form['fid']
        new_post = request.form['new_postid']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE PostForView SET (ID, FID, POSTID) = (%s,%s, %s) WHERE ID = '""" +id + """' AND FID = '""" +fid + """'"""

            cursor.execute(query, (id, fid, new_post))
            connection.commit()


    return render_template('add_post.html', posts=posts)
#End of Ahmet Caglar Bayatli's space

@app.route('/initdb')
def initialize_db():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        initialize_db_func(cursor)
        connection.commit()
    return redirect(url_for('home_page'))

@app.route('/count')
def counter_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()

        query = "UPDATE COUNTER SET N = N + 1"
        cursor.execute(query)
        connection.commit()

        query = "SELECT N FROM COUNTER"
        cursor.execute(query)
        count = cursor.fetchone()[0]
    return "This page was accessed %d times." % count


@app.route('/explore')
def explore_page():
    hashs = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT hashTag.HASHID, hashTag.GRUPNAME FROM hashTag"""

        cursor.execute(query)

        for hash in cursor:
            hashs.append(hash)

        connection.commit()

    return render_template('explore.html', hashs=hashs)

@app.route('/add_hash', methods = ['GET','POST'])
def add_hash():
    hashs = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT hashTag.HASHID, hashTag.GRUPNAME FROM hashTag"""

        cursor.execute(query)

        for hash in cursor:
            hashs.append(hash)

        connection.commit()


    if request.method =='POST':
        hashid = request.form['hashid']
        grupname = request.form['grupname']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO hashTag (HASHID, GRUPNAME ) VALUES (%s, %s )"""
            cursor.execute(query, (hashid, grupname))
            connection.commit()

    return render_template('add_hash.html', hashs=hashs)

@app.route('/delete_hash', methods = ['GET','POST'])
def delete_hash():
    hashs = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT hashTag.HASHID, hashTag.GRUPNAME FROM hashTag"""

        cursor.execute(query)

        for hash in cursor:
            hashs.append(hash)

        connection.commit()
    if request.method =='POST':
        hashid = request.form['hashid']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM hashTag WHERE HASHID = '""" +hashid + """'"""
            cursor.execute(query)
            connection.commit()

    return render_template('add_hash.html', hashs=hashs)

@app.route('/update_hash', methods = ['GET','POST'])
def update_hash():
    hashs = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT hashTag.HASHID, hashTag.GRUPNAME FROM hashTag"""

        cursor.execute(query)

        for hash in cursor:
            hashs.append(hash)

        connection.commit()

    if request.method =='POST':
        hashid = request.form['hashid']
        new_grupname = request.form['new_grupname']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE hashTag SET (HASHID, GRUPNAME ) = (%s,%s ) WHERE HASHID = '""" +hashid + """'"""

            cursor.execute(query, (hashid, new_grupname))
            connection.commit()


    return render_template('add_hash.html', hashs=hashs)

@app.route('/notifications')
def notification_page():
    now = datetime.datetime.now()
    return render_template('notification.html', current_time=now.ctime())

@app.route('/profile', methods = ['GET','POST'])
def profile_page():
    now = datetime.datetime.now()
    images = []
    kullanici=[]
    userr=[]
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """select users.id,userlogin.username from users,userlogin where users.username=userlogin.username"""
        cursor.execute(query)
        for im in cursor:
            kullanici.append(im)

        query = """select users.id,posts.link from users,posts where userid=3 and users.id=posts.userid"""
        cursor.execute(query)
        for im in cursor:
            images.append(im)


        query="""select userid,link, username, name, surname,mail from profilepic,users where userid=3 and users.id=profilepic.userid"""
        cursor.execute(query)
        for us in cursor:
            userr.append(us)

        connection.commit()
    if request.method =='POST':
        if 'ADD' in request.form:
            Image = request.form['ADD']
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO POSTS (USERID,LINK ) VALUES (3,'%s' )"""%Image
                cursor.execute(query)
                connection.commit()
            return redirect(url_for('profile_page'))
        if 'Change' in request.form:

            return redirect(url_for('profile_page'))
    return render_template('profile.html', current_time=now.ctime(),images=images,userr=userr,kullanici=kullanici)

@app.route('/add_pic', methods = ['GET','POST'])
def add_pic():
    pics = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT picPost.PicId, picPost.Description FROM picPost"""

        cursor.execute(query)

        for pic in cursor:
            pics.append(pic)

        connection.commit()
    if request.method =='POST':
        if 'ADD' in request.form:
            picDesc = request.form['ADD']
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO picPost (Description ) VALUES ('%s' )"""%picDesc
                cursor.execute(query)
                connection.commit()
            return redirect(url_for('add_pic'))

        if 'Delete' in request.form:
            picId=request.form['id']
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """DELETE FROM picPost WHERE PicId = '""" +picId + """'"""
                cursor.execute(query)
                connection.commit()
            return redirect(url_for('add_pic'))

        if 'Update' in request.form:
            picId=request.form['id']
            Desc = request.form['newname']
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """UPDATE picPost SET (Description ) = ('"""+Desc+"""') WHERE PicId = '""" +picId + """'"""
                cursor.execute(query)

                connection.commit()
            return redirect(url_for('add_pic'))

    return render_template('add_pic.html', pics=pics)

@app.route('/deneme', methods = ['GET','POST'])
def deneme_page():
    images = []
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT ID,LINK FROM POSTS"""

        cursor.execute(query)

        for im in cursor:
            images.append(im)
        connection.commit()

    if request.method =='POST':
        if 'ADD' in request.form:
            Image = request.form['ADD']
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO IMAGES (IMAGE ) VALUES ('%s' )"""%Image
                cursor.execute(query)
                connection.commit()
            return redirect(url_for('deneme_page'))

    return render_template('deneme.html',images=images)

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=5432 dbname='itucsdb'"""

    app.run(host='0.0.0.0', port=port, debug=debug)
