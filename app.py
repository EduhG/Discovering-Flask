from flask import Flask, render_template, request, url_for, \
    flash, redirect, session, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
# import sqlite3
# import os


app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from models import *


# Login required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    '''
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[1], description=row[2]) for row in cur.fetchall()]
    g.db.close()
    '''
    posts = db.session.query(BlogPost).all()

    return render_template('index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('welcome'))

'''
def connect_db():
    app.database = "posts.db"
    return sqlite3.connect(app.database)
'''

if __name__ == '__main__':
    app.run()
