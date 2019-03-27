import pytest
from random import randint
from random import choice
from faker import Faker
from libs.models.mimic_model import Mimic as mm
from libs.utils.db import DBHelper
from libs.utils.json import Writer


fake = Faker()

patient_db_cur = DBHelper(prefix="patients_mimic")
notes_db_cur = DBHelper(prefix="notes_mimic")
patient_json_cur = Writer()
notes_json_cur = Writer()
