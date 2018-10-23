#import modules
from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
from mysqlconnection import MySQLConnector 
import re
import os, binascii
import md5

#initialize global variables
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') 
ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall_db' )
app.secret_key = 'abcde12345fghij'

###Rendering Routes
#Route to login and Registration
@app.route('/')
def index():
    return render_template('index.html')

#registration route
@app.route('/register', methods=['POST'])
def create():
    #collect data from form
    email = request.form['email']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    password = request.form['password']
    confirm = request.form['confirm']
    errors = [] 
  
  # Validate Email
    if not Email_REGEX.match(email):
        errors.append('Invalid Email address')
    # Validate Name
    if (len(firstName) < 2) or (leng(lastName) < 2):
        errors.append('First and Last name must be at least 2 characters')
    
    if(not ALPHA_REGEX.match(firstName)) or (not ALPHA_REGEX.match(lastName)):
        errors.append('First and Last name cannot contain numbers or symbols')

    # Validate Password
    if password != confirm:
        errors.append("Passwords must match")

    if len(password) < 8:
        errors.append('Password must be at least 8 characters')

    # Check to see if they are already a user
    if not errors: 
        duplicates = mysql.query_db("SELECT * FROM users WHERE email= :email", {'email': email})    
        if duplicates:
            errors.append('This email has already been registered')
    
    # Attach errors to flash
    if errors:
        for error in errors:
            flash(error, 'error')
        return redirect('/')

    
    #Salt and insert password 

    # salt= binascii.b2a_hex(os.urandom(15))
    # hashed_pw = md5.new(password + salt).hexdigest() 
    # forgot to add salt to my users table, need to got back and edit 

    hashed_pw = md5.new(password).hexdigest() 
    insert = "INSERT INTO users (first_name, last_name, password, email, created_at, updated_at) VALUES (:first_name, :last_name, :password, :email, NOW(), NOW())"
    data = {'first_name': first_name, 'last_name': last_name, 'password': hashed_pw, 'email': email }
    mysql.query_db(insert, data)

 # login validation route
@app.route('/login', methods= ["POST"])
def login():
    # retrieve the user
    email = request.form['log_email']
    password = request.form['log_password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = { 'email': email}
    mysql.query_db(user_query, query_data)

    if user: 
        encrypted_password = md5.new(password ).hexdigest()
        if user[0]['password'] == encrypted_password:
            #save user in session and send to the wall
            session['uid'] = user[0]['id']
            return redirect('/wall')
        else: 
            #send invalid login back with flash error
            flash('Incorrect username or password', 'error')
            return redirect('/')
    else: 
        flash("Incorrect username or password", 'error')
        return redirect('/')

        
#route to post a message
@app.route('/message', methods= ["POST"])
def create_message():
    message = request.form['message_text']
    if len(message) < 1:
        flash("Message cannot be blank", "message")
        return redirect('/wall')
    elif len(message > 1 ) and (session['uid'])
        user = session['uid']
        query = "INSERT INTO messages (users_id, message, created_at, updated_at) VALUES (:uid, :message, NOW(), NOW())"
        data = { 'uid': user,
                'message': message}
        db_message = mysql.query_db(query, data)

        #redirect to see message
        url = '/wall#' + str(db_message)
        return redirect(url)  

@app.route('/comment/<message_id>', methods=['POST'])
def create_comment(message_id):
    comment = request.form['comment_text'] 
    message_id = 
    
#     if length < 2:
#         print "hello"
#         passFlag = False
#         print passFlag
#         flash('Email is invalid', 'register')
#     elif not EMAIL_REGEX.match(request.form['email']):
#         flash('Email is not in a valid format', 'register')
#         passFlag = False
#     elif len(request.form['first_name']) < 2:
#         flash('Name must be atleast two characters', 'register')
#         passFlag = False
#     elif len(request.form['last_name']) < 2:
#         flash('Last name must have atleast two characters', 'register')
#         passFlag = False
#     elif len(request.form['password']) < 8:
#         flash('Password needs to be 8 characters long', 'register')
#         passFlag = False
#     elif request.form['password'] != request.form['confirm']:
#         flash('Passwords do not match', 'register')
#         passFlag = False
#     print passFlag
#     if passFlag == False:
#         return redirect('/')
    
        
    
#     query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

#     data = {
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email'],
#         'password': request.form['password']
#     }
#     mysql.query_db(query, data)
#     return redirect('/wall')

# @app.route('/wall', methods=['GET'])
# def wallin():
#     query = "SELECT first_name, email FROM users"
#     users = mysql.query_db(query)
#     tin =  users[0]['first_name']
#     print tin
#     data = {
#         "tin": tin,
#         "users":users
#     }
#     return render_template('wall.html', users = users)

# @app.route('/login', methods=["POST"])
# def login():
#     print "hello"
#     passFlag = True
#     query = "SELECT * from users WHERE email = :email"
#     data = {
#         'email': request.form['log_email']
#     }
#     return render_template('wall.html')
#     user = mysql.query_db(query, data)
#     print user
#     if not EMAIL.REGREX.match(request.form['log_email']):
#         passFlag = False
#         flash('Email needs to include @ and . ', 'login')
    
    


# app.run(debug=True)