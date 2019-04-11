from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


app = Flask(__name__)

db = SQLAlchemy()
from models import db

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'datacatalog',
    'host': 'ec2-34-211-128-184.us-west-2.compute.amazonaws.com',
    'port': '5432',
}
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

from models import DataPortal

@app.route("/")
def main():
    return 'Data Portal List'


@app.route("/getall")
def get_all():
    try:
        dataPortal=DataPortal.query.all()
        return  jsonify([e.serialize() for e in dataPortal])
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':

    app.run()

