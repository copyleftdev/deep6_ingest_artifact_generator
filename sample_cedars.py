import pytest
from random import randint
from random import choice
from faker import Faker
from libs.models.cedars_model import Cedars as cm
from libs.utils.db import DBHelper
from libs.utils.csv import Writer

fake = Faker()
patient_db_cur = DBHelper(prefix="patients_cedars")
notes_db_cur = DBHelper(prefix="notes_cedars")
patient_csv_cur = Writer()
note_csv_cur = Writer()


for x in range(20):
    patientid = randint(00000000, 99999999)
    patient = cm.patient_fields
    note = cm.p_note_fields
    patient["patientMrn"] = str(patientid)
    patient["firstName"] = fake.first_name()
    patient["lastName"] = fake.last_name()
    patient["middleName"] = fake.last_name()
    patient["birthDate"] = fake.iso8601()
    patient["mortalityStatus"] = "ALIVE"
    patient["email"] = fake.ascii_safe_email()
    patient["phoneNumberWork"] = fake.phone_number()
    patient["phoneNumberCell"] = fake.phone_number()
    patient["phoneNumberHome"] = fake.phone_number()
    note["patientMrn"] = patientid
    note["noteText"] = "insert sample note here."
    patient_db_cur.insert_record(payload=patient)
    notes_db_cur.insert_record(payload=note)

patient_records = patient_db_cur.get_all_record()
note_records = notes_db_cur.get_all_record()
patient_csv_cur.save(records=patient_records, file_loc="data/sample_cedars_patients.csv")
note_csv_cur.save(records=note_records, file_loc="data/sample_cedars_notes.csv")
