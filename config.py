# Flask 및 데이터베이스 설정 파일

from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/dbname" # db설정
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 5
    SQLALCHEMY_POOL_RECYCLE = 1800
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_ECHO = False
    reload = True

'''
app.py, run.py

app = Flask(__name__)

같은 애들 한 곳에 모아서(초기설정)

'''