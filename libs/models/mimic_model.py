"""
Mimic Model
"""

class Mimic(object):
    """Mimic Fields"""

    cpt_fields = {
        "rowId": "",
        "subjectId": "",
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
        "rowId": "",
        "subjectId": "",
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
        "rowId": "",
        "itemId": "",
        "label": "",
        "fluid": "",
        "category": "",
        "loincCode": "",
    }

    icd9_fields = {"rowId": "", "icd9Code": "", "shortTitle": "", "longTitle": ""}

    iccd_diagnosis_fields = {
        "rowId": "",
        "subjectId": "",
        "hadmId": "",
        "seqNum": "",
        "icd9Code": "",
    }
    icu_stay_fields = {
        "rowId": "",
        "subjectId": "",
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
        "rowId": "",
        "subjectId": "",
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
        "rowId": "",
        "subjectId": "",
        "hadmId": "",
        "itemId": "",
        "chartTime": "",
        "value": "",
        "valueNum": "",
        "valueUOM": "",
        "flag": "",
    }

    prescription_fields = {
        "rowId": "",
        "subjectId": "",
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
