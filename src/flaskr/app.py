from flask import Flask
from flask import jsonify
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
from models import db

Bootstrap(app)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'datacatalog',
    'host': 'ec2-34-211-128-184.us-west-2.compute.amazonaws.com',
    'port': '5432',
}
app.config['DEBUG'] = True
DEBUG = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

from models import DataPortal


@app.route("/")
def main():
    # return 'Data Portal List'

    return render_template('base.html')


@app.route("/dataportal/getall")
def get_all():
    try:
        dataPortal = DataPortal.query.all()

        return render_template('getall.html', data=dataPortal)

        if request.args['type'] == 'json':
            data = jsonify([e.serialize() for e in dataPortal])
            return jsonify(data=data)
        else:
            return render_template('getall.html', data=dataPortal)





    except Exception as e:
        return (str(e))


if __name__ == '__main__':
    app.run()
