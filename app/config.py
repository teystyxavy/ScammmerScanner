import os

class Config:
    SECRET_KEY = b'\x85W\xfa,]w\xf5\xa6\xb5\xe4\xf2\x84\xb0\xcbl\x8b\xb7c\x0b\x87;\xfb,\xce'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESSERACT_PATH = os.environ.get('TESSERACT_PATH')
    VT_API_KEY = os.environ.get('VT_API_KEY')