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
    "ASIAN - VIETNAMESE",
    "MIDDLE EASTERN",
    "HISPANIC/LATINO - CENTRAL AMERICAN (OTHER)",
    "ASIAN - JAPANESE",
    "BLACK/CAPE VERDEAN",
    "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER",
    "SOUTH AMERICAN",
    "HISPANIC/LATINO - COLOMBIAN",
    "WHITE - OTHER EUROPEAN",
    "ASIAN - FILIPINO",
    "ASIAN - CHINESE",
    "HISPANIC/LATINO - HONDURAN",
    "HISPANIC/LATINO - PUERTO RICAN",
    "ASIAN - ASIAN INDIAN",
    "AMERICAN INDIAN/ALASKA NATIVE FEDERALLY RECOGNIZED TRIBE",
    "BLACK/AFRICAN AMERICAN",
    "ASIAN - CAMBODIAN",
    "WHITE",
    "ASIAN - THAI",
    "BLACK/AFRICAN",
    "PATIENT DECLINED TO ANSWER",
    "HISPANIC/LATINO - MEXICAN",
    "BLACK/HAITIAN",
    "HISPANIC/LATINO - GUATEMALAN",
    "PORTUGUESE",
    "ASIAN - OTHER",
    "UNKNOWN/NOT SPECIFIED",
    "OTHER",
    "HISPANIC/LATINO - SALVADORAN",
    "WHITE - RUSSIAN",
    "MULTI RACE ETHNICITY",
    "HISPANIC/LATINO - DOMINICAN",
    "WHITE - EASTERN EUROPEAN",
    "WHITE - BRAZILIAN",
    "HISPANIC/LATINO - CUBAN",
    "ASIAN - KOREAN",
    "AMERICAN INDIAN/ALASKA NATIVE",
    "CARIBBEAN ISLAND",
    "UNABLE TO OBTAIN",
    "ASIAN",
    "HISPANIC OR LATINO",
]

fake = Faker()
patient_db_cur = DBHelper(prefix="patients_mdanderson")
notes_db_cur = DBHelper(prefix="notes_mdanderson")
patient_csv_cur = Writer()
note_csv_cur = Writer()

site_id = str(uuid.uuid4()).replace("-", "")


for x in range(20):
    sex_salt = random.choice(["M", "F"])
    age = randint(15, 85)
    dob = moment.utcnow().subtract(years=age).strftime("%Y-%m-%d")
    patient_id = str(uuid.uuid4()).replace("-", "")
    patient = mdm.patient_fields
    note = mdm.note_field
    patient["siteId"] = site_id
    patient["ptMrn"] = patient_id
    if "M" in sex_salt:
        patient["firstName"] = fake.first_name_male()
    elif "F" in sex_salt:
        patient["firstName"] = fake.first_name_female()
    patient["lastName"] = fake.last_name()
    patient["dob"] = dob
    patient["ethnicity"] = random.choice(ethnicity_list)
    patient["sex"] = sex_salt
    patient["zip"] = fake.postcode_in_state(state_abbr="CA")
    patient["status"] = "Alive"
    note["siteId"] = site_id
    note["ptMrn"] = patient_id
    note["noteText"] = "sample file created for ingestion testing perposes"
    patient_db_cur.insert_record(payload=patient)
    notes_db_cur.insert_record(payload=note)


patient_records = patient_db_cur.get_all_record()
note_records = notes_db_cur.get_all_record()
print(patient_records)
print(note_records)
patient_csv_cur.save(
    record=patient_records, file_loc="data/sample_mdanderson_patients.csv"
)
note_csv_cur.save(record=note_records, file_loc="data/sample_mdanderson_notes.csv")
