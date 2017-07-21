'''Bucket list application'''

from flask import Flask, flash, session, render_template, escape, url_for, redirect, request
from app_functionality import User, BucketList

app = Flask(__name__)


@app.route('/')
def index():
    '''Returns rendered Homepage(Index page) of the app'''
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''Registers a new user, allowing them to use app'''
    if request.method == 'POST':
        email = request.form['email']
        user_name = request.form['user_name']
        password = request.form['password']
        if user_name and password and email:
            user = User(email, user_name, password)
            user.register_user()
            return redirect(url_for('create'))
        else:
            return render_template('register.html')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Logs in existing user to app'''
    if request.method == 'POST':
        email = None
        session['user_name'] = user_name = request.form['user_name']
        password = request.form['password']
        if user_name and password:
            user = User(email, user_name, password)
            if user_name in list(user.registered_users.keys()):
                if password == user.registered_users[user_name].password:
                    return redirect(url_for('view'))
                else:
                    flash('You entered the wrong password.')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    '''Returns rendered Create page'''
    if request.method == 'POST':
        title = session['title'] = request.form['Title']
        badge = session['badge'] = request.form['Badge']
        if title and badge:
            new_item = BucketList(title, badge)
            new_item.view_items()
            return redirect(url_for('view'))
        else:
            return render_template('create.html')
    else:
        return render_template('create.html')


@app.route('/view', methods=["GET", "POST"])
def view():
    '''Returns rendered View page'''
    if request.method == "POST":
        title = session.get('title')
        badge = session.get('badge')
            # return redirect(url_for('view'), title, badge)
        return render_template(('view.html', title, badge))


@app.route('/logout')
def logout():
    '''End user session'''
    session.pop('user_name', None)
    return redirect(url_for('index.html'))


app.secret_key = 'why-would-i-tell-you-this?'


if __name__ == '__main__':
    app.run(debug=True)
