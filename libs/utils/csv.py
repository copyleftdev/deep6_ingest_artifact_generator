"""Module to write records to file"""
import csv

class Writer(object):
    """Class to write dictionary to csv file"""

    def save(self, record, file_loc):
        """save method"""
        keys = record[0].keys()
        with open(file_loc, "w") as outcsv:
            writer = csv.DictWriter(outcsv, keys)
            writer.writeheader()
            writer.writerows(record)
