import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/database.db'
    SQLALCHEMY_DATABASE_URI= f'postgresql://{os.environ.get("POSTGRES_USER")}:' \
                                        f'{os.environ.get("POSTGRES_PASSWORD")}@' \
                                        f'{os.environ.get("POSTGRES_HOST")}:' \
                                        f'{os.environ.get("POSTGRES_PORT")}/' \
                                        f'{os.environ.get("POSTGRES_DB")}'