"""Example : Create  dataset for all current providers"""

from random import randint
from random import choice
from faker import Faker
from libs.models.athena_model import Athena as athena_m
from libs.models.austin_model import Austin as austin_m
from libs.models.cedars_model import Cedars as cedars_m
from libs.models.jefferson_model import Jefferson as jefferson_m
from libs.models.lifehouse_model import Lifehouse as lifehouse_m
from libs.models.mayo_model import Mayo as mayo_m
from libs.models.mdanderson_model import MdAndersion as mdanderson_m
from libs.models.mimic_model import Mimic as mimic_m
from libs.models.uhhospital_model import UhHospital as uh_m
from libs.models.upenn_model import Upenn as upenn_m
from libs.utils.db import DBHelper
from libs.utils.csv import Writer

fake = Faker()



# Faker  Variables
sex = choice(['M','F'])
male_first_name = fake.first_name_male()
female_first_name = fake.first_name_female()
last_name = fake.last_name()
dob = fake.iso8601()


def insert_record(prefix=None, record=None):
    cur = DBHelper(prefix=prefix)
    cur.insert_record(record)

def write_csv(records, client_name):
    cur = Writer()
    cur.save(record=patients ,file_loc= "data/sample_{}_.csv")

def gen_athena(patient_mrn, note_seed):
    model = athena_m()

    patient = model.patient_fields
    note = model.note_fields

    if 'M' in sex:
        patient["fistName"] = male_first_name
    elif 'F' in sex:
        patient["fistName"] = female_first_name
    patient['lastName'] = last_name
    patient['sex'] = sex
    patient['dob'] = dob
    patient['status'] = 'Alive'
    note['ptMrn'] = patient_mrn
    note['noteText'] = note_seed
    return {"patient": patient, "note": note}


print(gen_athena('3456675', 'insert notes'))

def gen_austin(count=1):
    pass

def gen_cedars(count=1):
    pass

def gen_jefferson(count=1):
    pass

def gen_lifehouse(count=1):
    pass

def gen_mayo(count=1):
    pass

def gen_mdanderson(count=1):
    pass

def gen_mimic(count=1):
    pass

def gen_uhhisptal(count=1):
    pass

def upenn_model(count=1):
    pass
