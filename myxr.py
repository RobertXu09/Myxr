import flask # Flask, request, abort, url_for, session, redirect, flash, render_template
import csv
import records

#init
app = flask.Flask(__name__)

# config
app.config['SECRET_KEY'] = "i forget why i need this tbh"

db = records.Database('sqlite:///myxr.db')

# command line handlers
@app.cli.command('initdb')
def initdb_command():
    # create database
    db.query('DROP TABLE IF EXISTS drinks')
    db.query('CREATE TABLE drinks (key int PRIMARY KEY, name text, ingredients text')

    # add contents of csv file to database
    with open('/resources/ingredients.csv', newline = '') as csv_file:
        csv_reader = csv.reader(csv_file)
    return

# routes
@app.route('/index/')
def index():
    pass