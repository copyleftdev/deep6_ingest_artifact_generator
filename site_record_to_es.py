import requests
from faker import Faker
import random
import json
import moment
import uuid

fake = Faker()
site_ids = [11111111,22222222,33333333,44444444,
               55555555,66666666,77777777,88888888,99999999]

es_host = 'http://es1.qa1.deep6.ai:9200/site-index-v1/doc'
post_head = {"Content-Type": "application/json"}


aws_regions = ["us-east-1", "us-east-2", "us-west-1", "ap-southeast-2"]
site_record_pl = {
    "addressLine1":"",
    "addressLine2":"",
    "addressLine3":"",
    "city":"",
    "email":"",
    "latitude":"",
    "longitude":"",
    "phone":"",
    "postalCode":"",
    "region":"",
    "siteId":"",
    "siteName":"",
    "url":"",
}

patient_record_pl =  {
    "age":"",
    "birthDate":"",
    "deathDate": "",
    "ethnicity":"",
    "firstName":"",
    "gender":"",
    "hasResearchOptOut":"", #bool None Not Allowed,
    "height":"",
    "isConfidential":"", # bool None Not Allowed
    "lastName":"",
    "middleName":"",
    "mortalityStatus":"Alive",
    "mrn": "",
    "races":"",
    "uuid":"",
    "weight":"",
    "siteId":"",

}

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

def gen_site_ids():
    insert_index = 0
    for site in site_ids:
        lat_long = fake.location_on_land(coords_only=True)
        site_record_pl['addressLine1'] = fake.address().replace("\n"," ")
        site_record_pl['addressLine2'] = fake.address().replace("\n"," ")
        site_record_pl['addressLine3'] = fake.address().replace("\n"," ")
        site_record_pl['city'] = fake.city()
        site_record_pl['email'] = fake.safe_email()
        site_record_pl['latitude'] = lat_long[0]
        site_record_pl['longitude'] = lat_long[1]
        site_record_pl['phone'] = fake.phone_number()
        site_record_pl['postalCode'] = fake.postcode_in_state(state_abbr="CA")
        site_record_pl['region'] = random.choice(aws_regions)
        site_record_pl['siteId'] = site
        site_record_pl['siteName'] = "Test Site #{}".format(insert_index)
        site_record_pl['url'] = "http://www.example.com"
        req = requests.put(es_host + "/{}".format(insert_index), headers=post_head,data=json.dumps(site_record_pl))
        insert_index += 1
        print(req.json())

def gen_patient():
    age = random.randint(18, 84)
    SEX_RND = random.choice(['M','F'])
    patient_record_pl['gender'] = SEX_RND
    if  "M" in SEX_RND:
        patient_record_pl['firstName'] = fake.first_name_male()
    elif "F" in SEX_RND:
        patient_record_pl['firtName'] = fake.first_name_female()
    else:
        patient_record_pl['firstName'] = "[T]User"
    patient_record_pl['lastName'] = fake.last_name()
    patient_record_pl['age'] = age
    patient_record_pl['birthDate']  = moment.utcnow().subtract(years=age).strftime("%Y-%m-%d")
    patient_record_pl['ethnicity'] = random.choice(ethnicity_list)
    patient_record_pl['hasResearchOptOut'] = random.choice([True, False])
    patient_record_pl['isConfidential'] = random.choice([True, False])
    patient_record_pl['mrn'] = str(uuid.uuid4()).replace("-","")
    

    print(patient_record_pl)


for x in range(100):
    gen_patient()