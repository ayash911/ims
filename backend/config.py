from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://username:password@localhost/ims')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
