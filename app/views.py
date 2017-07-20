'''Bucket list application'''

from flask import Flask, flash, session, abort, render_template, url_for, redirect, request
from app_functionality import User, BucketList

app = Flask(__name__)


@app.route('/')
def index():
    '''Returns rendered Homepage(Index page) of the app'''
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return "Welcome to le BucketListApp"


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''Registers a new user, allowing them to use app'''

    if request.method == 'POST':
        email = request.form['exampleInputEmail1']
        user_name = request.form['exampleInputUserName']
        password = request.form['exampleInputPassword1']
        if user_name and password and email:
            user = User(email, user_name, password)
            user.register_user()
            return redirect(url_for('create'))
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST'])
def login():
    '''Logs in existing user to app'''
    email = None
    user_name = request.form['exampleInputUsername']
    password = request.form['exampleInputPassword1']
    if user_name and password:
        user = User(email, user_name, password)
        if user_name in list(user.registered_users.keys()):
            if password == user.registered_users[user_name].password:
                session['logged_in'] = True
            else:
                flash('You entered the wrong password.')
                
        else:
            render_template('login.html')
    else:
        render_template('login.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    '''Returns rendered Create page'''
    if request.method == 'POST':
        title = request.form['exampleInputTitle']
        badge = request.form['exampleInputBadge']
        if title and badge:
            new_item = BucketList(title, badge)
            new_item.view_items()
            return redirect(url_for('view'))
        else:
            return render_template('create.html')
    else:
        return render_template('create.html')


@app.route('/view')
def view():
    '''Returns rendered View page'''
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)
