"""
DB Helper for  TinyDB
"""
import time
from tinydb import TinyDB, Query



class DBHelper(object):

    def __init__(self, prefix):
        
        self.db = TinyDB('db/{}.db'.format(prefix))

    def insert_record(self, payload):
        """Insert Record"""
        self.db.insert(payload)

    def get_all_record(self):
        return self.db.all()
