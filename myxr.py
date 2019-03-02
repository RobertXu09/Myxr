import flask # Flask, request, abort, url_for, session, redirect, flash, render_template
import models # db, Owner, Stylist, Patron, Appointment
import csv
import records

#init
app = flask.Flask(__name__)

# config
SECRET_KEY = "i forget why i need this tbh"
SQLALCHEMY_DATABASE_URI = "sqlite:///myxr.db" # we'll probably change this

app.config.from_object(__name__)

db = records.Database('sqlite:///myxr.db')

# command line handlers
@app.cli.command('run')
def run_command():
    # add contents of csv file to database
    pass
