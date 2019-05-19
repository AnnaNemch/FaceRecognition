from sqlalchemy import Column, Integer, String
from ..services.database import Base, session
from marshmallow import Schema, fields, pprint

class User(Base):
    """ User Model for storing user related details """
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    password = Column(String, nullable=False)
    # TODO :: add field isGuest and user_name

    def __init__(self, first_name, last_name, email, phone, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(Schema):
    """ Serializable User Schema """
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    phone = fields.Str()
    