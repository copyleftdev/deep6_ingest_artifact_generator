"""
MDAnderson Model
"""


class MdAndersion(object):
    """danderson fields"""

    allergy_fields = {
        "siteId": "",
        "patientMrn": "",
        "allergen": "",
        "allergenType": "",
        "allergyType": "",
        "reactions": "",
        "severityLevel": "",
        "reactionComment": "",
        "enteredDate": "",
    }
    encounter_fields = {
        "siteId": "",
        "ptMrn": "",
        "encId": "",
        "encAdmitDttm": "",
        "encDischargeDttm": "",
        "admitProvider": "",
        "attendProvider": "",
        "referProvider": "",
        "pcpProvider": "",
        "consultProvider": "",
        "encMajorType": "",
        "encPatientClass": "",
        "admitSrc": "",
        "encStatus1": "",
        "encStatus2": "",
        "admissionType": "",
        "chiefComplaint": "",
        "dxCode": "",
        "admitDx": "",
        "admitDxText": "",
    }

    genomic_report_fields = {
        "siteId": "",
        "ptMrn": "",
        "reportDttm": "",
        "reportId": "",
        "reportText": "",
        "geneCodes": "",
    }
    imaging_report_fields = {
        "siteId": "",
        "ptMrn": "",
        "orderId": "",
        "orderProvider": "",
        "authProvider": "",
        "finalProvider": "",
        "dictateProvider": "",
        "collectionDttm": "",
        "resultDttm": "",
        "addendNoteId": "",
        "addendDttm": "",
        "imgResultText": "",
        "addendResultText": "",
        "encId": "",
    }
    lab_report_fields = {
        "siteId": "",
        "ptMrn": "",
        "labOrderId": "",
        "labLineNo": "",
        "labLoinc": "",
        "labProcedure": "",
        "labRsltCollectionDttm": "",
        "labRsltDttm": "",
        "labRsltValue": "",
        "labRsltUom": "",
        "labDataType": "",
        "resultingLab": "",
        "labProcComments": "",
        "labTestComment": "",
        "encId": "",
    }
    mar_fields = {
        "siteId": "",
        "ptMrn": "",
        "ordId": "",
        "ordMedDttm": "",
        "ordMedStartDttm": "",
        "ordMedEndDttm": "",
        "ordMedFrequency": "",
        "ordMedNoOfDoses": "",
        "ordMedNm": "",
        "ordMedRxNorm": "",
        "ordMedAmtMin": "",
        "ordMedAmtMax": "",
        "ordMedUnits": "",
        "orderingProvider": "",
        "authorizingProvider": "",
        "verifyingProvider": "",
        "instructions": "",
        "prnReasons": "",
        "encId": "",
    }
    note_field = {
        "siteId": "",
        "ptMrn": "",
        "noteId": "",
        "encounterType": "",
        "noteDos": "",
        "noteType": "",
        "noteCreateProvider": "",
        "noteSignProvider": "",
        "noteFirstSignDttm": "",
        "noteCurrentAuth": "",  # "contactDateReal":"", "line":"", "sort":"",
        "noteText": "",
        "encId": "",
    }
    pathology_report_fields = {
        "siteId": "",
        "ptMrn": "",
        "apOrderId": "",
        "apOrderStsCd": "",
        "resultDttm": "",
        "collectionDttm": "",
        "specimenSrcList": "",
        "orderMd": "",
        "resultMd": "",
        "resultText": "",
        "encId": "",
    }

    patient_fields = {
        "siteId": "",
        "ptMrn": "",
        "lastName": "",
        "firstName": "",
        "middleName": "",
        "dob": "",
        "ethnicity": "",
        "sex": "",
        "race": "",
        "zip": "",
        "deathDttm": "",
        "status": "",
        "weight": "",
        "height": "",
    }
