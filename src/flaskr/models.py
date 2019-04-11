
from flask_sqlalchemy import SQLAlchemy
import datetime



db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class DataPortal(db.Model):
    __tablename__ = 'dataportal'
    id = db.Column(db.Integer, primary_key=True)
    id_name = db.Column(db.String())
    name = db.Column(db.String())
    title = db.Column(db.String())
    url = db.Column(db.String())
    author = db.Column(db.String())
    publisher = db.Column(db.String())
    issued = db.Column(db.String())
    publisher_classification = db.Column(db.String())
    description = db.Column(db.String())
    tags = db.Column(db.String())
    license_id = db.Column(db.String())
    license_url = db.Column(db.String())
    place = db.Column(db.String())
    location = db.Column(db.String())
    country = db.Column(db.String())
    language = db.Column(db.String())
    status = db.Column(db.String())
    metadatacreated = db.Column(db.String())
    generator = db.Column(db.String())
    api_endpoint = db.Column(db.String())
    api_type = db.Column(db.String())
    full_metadata_download = db.Column(db.String())
    description_html = db.Column(db.String())
    groups = db.Column(db.String())
    dc_status = db.Column(db.String())
    user_created = db.Column('user_created', db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    user_updated = db.Column('user_updated', db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    insert_date  = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __init__(self, id_name, name, title, url, author, publisher, issued,
                         publisher_classification, description, tags, license_id, license_url,
                         place, location, country, language, status, metadatacreated,
                         generator, api_endpoint, api_type, full_metadata_download,
                         description_html, groups, dc_status, user_created,
                         user_updated, insert_date,updated_date):
        self.id = id
        self.id_name = id_name
        self.name = name
        self.title = title
        self.url = url
        self.author = author
        self.publisher = publisher
        self.issued = issued
        self.publisher_classification = publisher_classification
        self.description = description
        self.tags = tags
        self.license_id = license_id
        self.license_url = license_url
        self.place = place
        self.location = location
        self.country = country
        self.language = language
        self.status = status
        self.metadatacreated = metadatacreated
        self.generator = generator
        self.api_endpoint = api_endpoint
        self.api_type = api_type
        self.full_metadata_download = full_metadata_download
        self.description_html = description_html
        self.groups = groups
        self.dc_status = dc_status
        self.user_created = user_created
        self.user_updated = user_updated
        self.insert_date = insert_date
        self.updated_date = updated_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'id_name': self.id_name,
            'name': self.name,
            'title': self.title,
            'url': self.url,
            'author': self.author,
            'publisher': self.publisher,
            'issued': self.issued,
            'publisher_classification': self.publisher_classification,
            'description': self.description,
            'tags': self.tags,
            'license_id': self.license_id,
            'license_url': self.license_url,
            'place': self.place,
            'location': self.location,
            'country': self.country,
            'language': self.language,
            'status': self.status,
            'metadatacreated': self.metadatacreated,
            'generator': self.generator,
            'api_endpoint': self.api_endpoint,
            'api_type': self.api_type,
            'full_metadata_download': self.full_metadata_download,
            'description_html': self.description_html,
            'groups': self.groups,
            'dc_status': self.dc_status,
            'user_created': self.user_created,
            'user_updated': self.user_updated,
            'insert_date': self.insert_date,
            'updated_date': self.updated_date
        }