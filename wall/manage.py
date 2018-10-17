from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
from mysqlconnection import MySQLConnector 

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') 
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall_db' )
app.secret_key = 'abcde12345fghij'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create():
    passFlag= True
    length = len(request.form['email'])
    print length
    if length < 2:
        print "hello"
        passFlag = False
        print passFlag
        flash('Email is invalid', 'register')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email is not in a valid format', 'register')
        passFlag = False
    elif len(request.form['first_name']) < 2:
        flash('Name must be atleast two characters', 'register')
        passFlag = False
    elif len(request.form['last_name']) < 2:
        flash('Last name must have atleast two characters', 'register')
        passFlag = False
    elif len(request.form['password']) < 8:
        flash('Password needs to be 8 characters long', 'register')
        passFlag = False
    elif request.form['password'] != request.form['confirm']:
        flash('Passwords do not match', 'register')
        passFlag = False
    print passFlag
    if passFlag == False:
        return redirect('/')
    
        
    
    query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall', methods=['GET'])
def wallin():
    query = "SELECT first_name, email FROM users"
    users = mysql.query_db(query)
    tin =  users[0]['first_name']
    print tin
    data = {
        "tin": tin,
        "users":users
    }
    return render_template('wall.html', users = users)


app.run(debug=True)