import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:aracena@localhost/salon_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
