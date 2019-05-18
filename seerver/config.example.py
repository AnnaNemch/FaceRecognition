import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # db settings
    DB_URL = os.environ.get('DB_URL') or ""
    DB_name = os.environ.get('DB_name') or ""
    DB_user = os.environ.get('DB_user') or ""
    DB_password = os.environ.get('DB_password') or ""

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_user}:{DB_password}@{DB_URL}/{DB_name}'
   
    # camera settings
    CAMERA_ID = 0

    # settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or ""