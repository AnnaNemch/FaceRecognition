import os
basedir = os.path.abspath(os.path.dirname(__file__))

# TODO :: add to gitignore


class Config(object):
    # db settings
    DB_URL = "localhost:5432"
    DB_name = "FaceRecognition"
    DB_user = "postgres"
    DB_password = "root"

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_user}:{DB_password}@{DB_URL}/{DB_name}'
    SECRET_KEY = 'you-will-never-guess'
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # camera settings
    CAMERA_ID = 1
