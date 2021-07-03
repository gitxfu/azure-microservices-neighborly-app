import os

class Config(object):
    MONGO_URL = os.environ.get('MongoDBConnString')
    MONGO_DB_NAME = os.environ.get('MongoDBName')