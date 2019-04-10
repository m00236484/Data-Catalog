# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from models import db



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'datacatalog',
    'host': 'ec2-34-211-128-184.us-west-2.compute.amazonaws.com',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()