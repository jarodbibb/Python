from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector


app= Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', all_friends = friendss)
@app.route('/friends', methods=['POST'])
def create():
    #add a friend to the db 
    return redirect('/')
app.run(debug=True)