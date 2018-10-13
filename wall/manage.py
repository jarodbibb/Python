from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
from mysqlconnection import MySQLConnector 

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall_db' )
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/register', methods=['POST'])
# def create()


app.run(debug= True)