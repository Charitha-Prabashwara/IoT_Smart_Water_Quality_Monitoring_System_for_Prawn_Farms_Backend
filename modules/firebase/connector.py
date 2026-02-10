import firebase_admin 
from firebase_admin import db, credentials
from dotenv import load_dotenv


def connect(certificate, databaseURL):
    _credentials = credentials.Certificate(certificate)
    firebase_admin.initialize_app(_credentials, {"databaseURL":databaseURL})

    return db
