import pytest
from random import randint
from random import choice
from faker import Faker
from libs.models.athena_model import Athena as am
from libs.utils.db import DBHelper
from libs.utils.csv import Writer

fake = Faker()
patient_db_cur = DBHelper(prefix="patients_athena")
notes_db_cur = DBHelper(prefix="notes_athena")
patient_csv_cur = Writer()
note_csv_cur = Writer()


for x in range(100):
    patientid = randint(00000000, 99999999)
    patient = am.patient_fields
    note = am.note_fields
    patient['ptMrn'] = str(patientid)
    patient['firstName'] = fake.first_name()
    patient['lastName'] = fake.last_name()
    patient['middleName'] = fake.last_name()
    patient['dob'] = fake.iso8601()
    note['ptMrn'] = patientid
    note['noteText'] = "insert sample note here."
    patient_db_cur.insert_record(payload=patient)
    notes_db_cur.insert_record(payload=note)

patient_records = patient_db_cur.get_all_record()
note_records = notes_db_cur.get_all_record()
patient_csv_cur.save(records=patient_records, file_loc="data/sample_athena_patients.csv")
note_csv_cur.save(records=note_records, file_loc="data/sample_athena_notes.csv")
