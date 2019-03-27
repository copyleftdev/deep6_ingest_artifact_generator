"""Model to write records to json file"""
import json


class Writer(object):
    """Class to write dictionary to json file"""
    def save(self, record, file_loc):
        with open(file_loc, 'w') as jout:
            json.dump(record, jout)
