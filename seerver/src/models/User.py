from sqlalchemy import Column, Integer, String
import jwt
from ..services.database import Base, session
from flask import current_app
from marshmallow import Schema, fields, pprint
from app import ma

class User(Base):
    """ User Model for storing user related details """
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    password = Column(String, nullable=False)

    def __init__(self, first_name, last_name, email, phone, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('first_name', 'last_name', 'email', 'phone')

user_schema = UserSchema()

