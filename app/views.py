'''Bucket list application'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''Returns rendered Homepage(Index page) of the app'''
    return render_template('index.html')

@app.route('/login')
def login():
    '''Returns rendered Login page'''
    return render_template('login.html')

@app.route('/register')
def register():
    '''Returns rendered Register page'''
    return render_template('register.html')

@app.route('/view')
def view():
    '''Returns rendered View page'''
    return render_template('view.html')

@app.route('/create')
def create():
    '''Returns rendered Create page'''
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
