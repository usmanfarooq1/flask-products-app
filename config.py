import os

# setting up base directory for the database
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(BASE_DIRECTORY, 'products.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
