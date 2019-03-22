import pytest
from random import randint
from faker import Faker
fake = Faker()
from libs.models.athena_model import Athena as am

patientid = randint(00000000, 99999999)
patient = am.patient_fields
patient['ptMrn'] = str(patientid)
patient['firstName'] = "Don"
