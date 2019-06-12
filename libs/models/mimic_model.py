"""
Mimic Model
"""


class Mimic(object):
    """Mimic Fields"""

    cpt_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "costCenter": "",
        "chartDate": "",
        "cptCode": "",
        "cptNumber": "",
        "cptSuffix": "",
        "ticketIdSeq": "",
        "sectionHeader": "",
        "subsectionHeader": "",
        "description": "",
    }
    admission_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "admitTime": "",
        "dischTime": "",
        "deathTime": "",
        "admissionType": "",
        "admmissionLocation": "",
        "dischargeLocation": "",
        "insurance": "",
        "language": "",
        "religion": "",
        "matialStatus": "",
        "ethnicity": "",
        "edRegTime": "",
        "edOutTime": "",
        "diagnosis": "",
        "hospitalExpireFlag": "",
        "hasCharEventData": "",
    }
    d_lab_item_fields = {
        "ROW_ID": "",
        "itemId": "",
        "label": "",
        "fluid": "",
        "category": "",
        "loincCode": "",
    }

    icd9_fields = {"ROW_ID": "", "icd9Code": "", "shortTitle": "", "longTitle": ""}

    iccd_diagnosis_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "seqNum": "",
        "icd9Code": "",
    }
    icu_stay_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "icuStayId": "",
        "dbSource": "",
        "firstCareUnit": "",
        "lastCareUnit": "",
        "firstWardId": "",
        "lastWardId": "",
        "inTime": "",
        "outTime": "",
        "los": "",
    }
    physician_notes_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "chartDate": "",
        "chartTime": "",
        "storeTime": "",
        "category": "",
        "description": "",
        "cgId": "",
        "isError": "",
        "text": "",
    }

    lab_report_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "itemId": "",
        "chartTime": "",
        "value": "",
        "valueNum": "",
        "valueUOM": "",
        "flag": "",
    }

    prescription_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "hadmId": "",
        "icuStayId": "",
        "startDate": "",
        "endDate": "",
        "drugType": "",
        "drug": "",
        "drugNamePOE": "",
        "drugNameGeneric": "",
        "forumularyDrugCode": "",
        "gsn": "",
        "ndc": "",
        "prodStrength": "",
        "doseValRx": "",
        "doseUnitRx": "",
        "formValDisp": "",
        "formUnitDisp": "",
        "route": "",
    }

    provider_fields = {
        "providerId": "",
        "lastName": "",
        "middleName": "",
        "firstName": "",
        "providerType": "",
        "specialty": "",
    }
    patient_fields = {
        "ROW_ID": "",
        "SUBJECT_ID": "",
        "GENDER": "",
        "DATE_OF_BIRTH": "",
        "dateOfDeath": "",
        "DOD_HOSPITAL": "",
        "DOD_SSN": "",
        "EXPIRE_FLAG": "",
    }
