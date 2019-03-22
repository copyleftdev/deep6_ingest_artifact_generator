"""Module to write records to file"""
import csv

class Writer(object):
    """Class to write dictionary to csv file"""
    def __init__(self, file_name=None):
        self.file_name = file_name


    def save(self, record):
        """save method"""
        keys = record[0].keys()
        with open("sample_patients.csv", "wb") as outcsv:
            writer = csv.DictWriter(outcsv, keys)
            writer.writeheader()
            writer.writerows(record)
