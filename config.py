import os
import mongomock


class Config:
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGODB_DB"),
        "host": os.getenv("MONGODB_HOST"),
        "username": os.getenv("MONGODB_USER"),
        "password": os.getenv("MONGODB_PASSWORD")
    }


class DevConfig(Config):
    pass


class MockConfig(Config):
    MONGODB_SETTINGS = {
        "db": "test",
        "host": "mongodb://localhost",
        "mongo_client_class": mongomock.MongoClient
    }
