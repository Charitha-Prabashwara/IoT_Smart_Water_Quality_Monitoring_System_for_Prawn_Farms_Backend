import sqlite3
import os


APP_ROOT = os.getcwd()
DB_PATH = os.path.join(APP_ROOT, "database/data.db")

def connect():
   
    connection = sqlite3.connect(DB_PATH,check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection


