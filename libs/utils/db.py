"""
DB Helper for  TinyDB
"""
import time
from tinydb import TinyDB, Query



class DBHelper(object):

    def __init__(self, prefix):
        db_name = str(int(time.time()))
        self.db = TinyDB('db/{}_{}.db'.format(prefix, db_name))

    def insert_record(self, payload):
        """Insert Record"""
        self.db.insert(payload)

    def get_all_record(self):
        return self.db.all()
