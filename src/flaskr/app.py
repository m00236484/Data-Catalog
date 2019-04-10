from flask_sqlalchemy import SQLAlchemy
from models import db


app = Flask(__name__)

db = SQLAlchemy()
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


@app.route("/")
def main():
    return 'Hello World !'

if __name__ == '__main__':

    app.run()

