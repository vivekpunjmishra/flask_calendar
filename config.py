import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Database connection
username = os.getenv("DB_USERNAME", "root")
password = os.getenv("DB_PASSWORD", "Vivek123")
server = os.getenv("DB_HOST", "localhost")
database = os.getenv("DB_NAME", "calendar")

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(username, password, server, database)
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False