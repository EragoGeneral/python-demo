﻿from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    list = [1, 2, 3, 4, 5, 6]
    if username == 'admin' and password == '123456':
        return render_template('signin-ok.html', username=username, pageList = list)
    return render_template('form.html', message='Bas username or password', username=username)

if __name__ == '__main__':
    app.run()