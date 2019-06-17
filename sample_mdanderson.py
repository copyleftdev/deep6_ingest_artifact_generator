import uuid
import random
from random import randint
from random import choice
from faker import Faker
import moment
from libs.models.mdanderson_model import MdAndersion as mdm
from libs.utils.db import DBHelper
from libs.utils.csv import Writer


ethnicity_list = [
    "American Indian or Alaska Native",
    "White or Caucasian",
    "Asian",
    "Black or African American",
    "Native Hawaiian or Other Pacific Islander",
    "Declined to Answer",
    "Unknown",
    "Other",
]

fake = Faker()
patient_db_cur = DBHelper(prefix="patients_mdanderson")
notes_db_cur = DBHelper(prefix="notes_mdanderson")
patient_csv_cur = Writer()
note_csv_cur = Writer()

site_id = str(uuid.uuid4()).replace("-", "")


for x in range(20):
    sex_salt = random.choice(["M", "F"])
    eths = []
    ethnicity = random.choice(ethnicity_list)
    age = randint(15, 85)
    dob = fake.iso8601()
    patient_id = random.randint(11111, 99999999)
    patient = mdm.patient_fields
    note = mdm.note_field
    patient["siteId"] = site_id
    patient["PT_MRN"] = patient_id
    if "M" in sex_salt:
        patient["firstName"] = fake.first_name_male()
    elif "F" in sex_salt:
        patient["firstName"] = fake.first_name_female()
    patient["lastName"] = fake.last_name()
    patient["dob"] = dob
    patient["sex"] = sex_salt
    # patient["ethnicity"] = random.choice(ethnicity_list)
    patient["zip"] = fake.postcode_in_state(state_abbr="CA")
    patient["status"] = "Alive"
    note["siteId"] = site_id
    note["PT_MRN"] = patient_id
    note["noteFirstSignDttm"] = fake.iso8601()
    note["noteText"] = "sample file created for ingestion testing perposes"
    patient_db_cur.insert_record(payload=patient)
    notes_db_cur.insert_record(payload=note)


patient_records = patient_db_cur.get_all_record()
note_records = notes_db_cur.get_all_record()
print(patient_records)
print(note_records)
patient_csv_cur.save(
    records=patient_records, file_loc="data/sample_mdanderson_patients.csv"
)
note_csv_cur.save(records=note_records, file_loc="data/sample_mdanderson_notes.csv")
