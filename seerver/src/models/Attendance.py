from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..services.database import Base
from marshmallow import Schema, fields, pprint

class Attendance(Base):
    """ Attendance Model for storing user attendance """
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    photo_link = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __init__(self, date_time, photo_link):
        self.date_time = date_time
        self.photo_link = photo_link

    def __repr__(self):
        return '<id {}>'.format(self.id)

class AttendanceSchema(Schema):
    """ Serializable Attendance Schema """
    id = fields.Str()
    date_time = fields.DateTime()
    photo_link = fields.Str()
    # TODO :: add user data
    # user_id = Column(Integer, ForeignKey("user.id"))
