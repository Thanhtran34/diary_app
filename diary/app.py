from asyncio.windows_events import NULL
from typing import List, Dict
from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import mysql.connector
import json
from datetime import datetime
import sys
import functools
from db import Database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

db_config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'diary_app'
}

db = Database(**db_config)

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor(dictionary=True)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return 

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.find_user_by_id(user_id)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            if db.find_user_by_username(username) is not None:
                error = 'User {} is already registered.'.format(username)

        if error is None:
            db.create_user(username, password)
            return redirect(url_for('login'))

        flash(error)
    return render_template('register.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = db.find_user_by_username(username)

        if user is None:
            error = 'Incorrect username.'
        elif not user['password'] == password:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['user_id']
            return redirect(url_for('diaries'))

        flash(error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/diaries', methods=('GET', 'POST'))
def diaries():

    if g.user is None:
        return redirect(url_for('login'))

    user_id = session.get('user_id')
    if request.method == 'POST':
        diary_name = request.form['diary_type']
        db.create_diary(user_id, diary_name)
    
    diaries = db.find_diary_by_user_id(user_id)
    return render_template('diaries.html', diaries = diaries)

@app.route('/diary/<diary_id>', methods=('GET', 'POST'))
def diary(diary_id):
    if g.user is None:
        return redirect(url_for('login'))

    user_id = session.get('user_id')

    diary = db.find_diary_by_id(diary_id)

    if diary['user_id'] != user_id:
        return redirect(url_for('diaries'))

    '''
    if request.method == 'POST':
        diary_name = request.form['diary_name']
        working_day = request.form['working_day']
        process = request.form['process']

        story = db.find_story_by_name(diary_name)

        if story is None:
            story_id = db.create_story(diary_name)
        else:
            story_id = story['story_id']

        db.create_diary_type(diary_id, story_id, diary_name, working_day, process)

    diaries = db.find_story_data_for_diary_by_story_id(diary_id)
    render_template('diary.html', diaries = diaries)
    '''
    
    return render_template('test.html')

@app.route('/story_detail')
def story_detail():
    if g.user is None:
        return redirect(url_for('login'))

    user_id = session.get('user_id')
    story_detail = db.find_story_details_by_user_id(user_id)

    return render_template('story_detail.html', stories = story_detail)

@app.route('/diary_list')
def diary_list():
    records = db.find_all_diary()

    return render_template('diary_list.html', records = records)

if __name__ == '__main__':
    app.run(host='0.0.0.0')