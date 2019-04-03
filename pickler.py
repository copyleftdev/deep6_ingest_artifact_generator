import json
from random import choice, randint, sample
from faker import Faker
import uuid
from libs.utils.json import Writer
import time

fake = Faker()


with open("sample/record.json", "r") as nin:
    record = json.loads(nin.read())

    ethnicity = [
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


# Patient #####################################################################


def gen_mimic_record(note_seed="INSERT NOTES HERE"):

    patient_root = record["patient"]
    patient_root["mrn"] = randint(000000000, 999999999)
    patient_root["gender"] = choice(["FEMALE", "MALE"])
    if "FEMALE" in patient_root["gender"]:

        patient_root["firstName"] = fake.first_name_female()
    else:
        patient_root["firstName"] = fake.first_name_male()

    patient_root["lastName"] = fake.last_name()
    patient_root["middleName"] = "TEST USER"
    patient_root["birthDate"] = fake.unix_time(
        end_datetime="now", start_datetime="-70y"
    )
    patient_root["mortalityStatus"] = "ALIVE"
    patient_root["deathDate"] = ""
    patient_root["ethnicity"] = choice(ethnicity)
    patient_root["races"] = sample(ethnicity, 3)
    patient_root["isConfidential"] = choice([True, False])
    patient_root["uuid"] = str(uuid.uuid4())
    patient_root["zip"] = fake.postcode()
    patient_root["email"] = fake.ascii_safe_email()
    patient_root["phoneNumberCell"] = fake.phone_number()
    patient_root["phoneNumberHome"] = fake.phone_number()
    patient_root["phoneNumberWork"] = fake.phone_number()

    note_root = record["event"]["physicianNote"]
    record['event']['contents'] = []
    note_root["noteText"] = note_seed

    with open("data/{}.json".format(str(time.time())), "w") as jout:
        json.dump(record, jout)


###############################################################################
note_1 = """
[TEST NEGATION FALSE]Major Surgical or Invasive Procedure:
none

History of Present Illness:
70 y/o male with PMHx of DM II, HTN, prostate adenocarcinoma
s/p
prostatectomy presented to [**Hospital3 **] with sudden onset
N/V/abdominal pain that began [**1-28**] in the am after breakfast.
"""
note_2 = """
[TEST NEGATION POSITIVE]CONCLUSION:

1) Globally enlarged pancreatic head associated with peripancreatic fluid and
significant major and minor pancreatic ductal dilatation.  Given the presence
of pancreatic head calcifications, and an intraductal apparently enhancing
component, and the absence of vascular occlusion or compression, the findings
are overall not suggestive of simple adenocarcinoma
.  Diagnostic
considerations include:
a) multifocal IPMT with an invasive intraductal component
b) acute and chronic pancreatitis with secondary biliary obstruction
C) a small non- visualized carcinoma with secondary pancreatitis.
"""
note_3 = """
[TEST NEGATION FALSE]
Allergies:
Patient recorded as having No Known Allergies to Drugs

Attending:[**First Name3 (LF) 297**]
Chief Complaint:
Upper GI Bleed

Major Surgical or Invasive Procedure:
Placement of Right Femoral Cordis

History of Present Illness:
The patient is a 73 y.o. female with h/o duodenal adenocarcinoma
"""
notes = [note_1, note_2, note_3]
for n in notes:
    gen_mimic_record(note_seed=n)
