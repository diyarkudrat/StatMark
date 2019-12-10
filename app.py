from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/user')
def user():
    return render_template('user.html')
