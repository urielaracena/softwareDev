import os
from urllib.parse import urlparse

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Get DATABASE_URL from environment or use development default
    database_url = os.environ.get('DATABASE_URL')
    
    # Handle Render's postgres:// vs postgresql:// issue
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = database_url or 'postgresql://postgres:aracena@localhost:5432/salon_db'