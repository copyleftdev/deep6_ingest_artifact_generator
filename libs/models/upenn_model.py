"""
Upenn Model
"""


class Upenn(object):
    """ fields for uppen"""

    encounter_fields = {
        "ptMrn": "",
        "encId": "",
        "encAdmitDttm": "",
        "encDischargeDttm": "",
        "encMajorType": "",
        "encPatientClass": "",
        "encStatus1": "",
        "encStatus2": "",
        "encAdmissionType": "",
        "chiefComplaint": "",
        "dxCode": "",
        "dxName": "",
        "dxType": "",
        "dxText": "",
        "dxLine": "",
        "ptWeight": "",
        "ptHeight": "",
    }
    lab_report_fields = {
        "ptMrn": "",
        "encId": "",
        "labOrderId": "",
        "labLineNo": "",
        "labResultId": "",
        "labLoinc": "",
        "labProcedure": "",
        "labRsltCollectionDttm": "",
        "labRsltDttm": "",
        "commonName": "",
        "labRsltValue": "",
        "labRsltUom": "",
    }

    note_fields = {
        "ptMrn": "",
        "encId": "",
        "noteId": "",
        "noteDos": "",
        "noteText": "",
        "noteType": "",
        "contactDateReal": "",
        "line": "",
        "sort": "",
    }

    pathology_report = {
        "ptMrn": "",
        "EncId": "",
        "apOrderId": "",
        "apOrderStsCd": "",
        "resultDttm": "",
        "collectionDttm": "",
        "apReportId": "",
        "specimenSrcList": "",
        "componentId": "",
        "componentName": "",
        "lineComment": "",
        "resultText": "",
        "apLineNo": "",
    }

    patient_fields = {
        "ptMrn": "",
        "ptName": "",
        "patLastName": "",
        "patFirstName": "",
        "patMiddleName": "",
        "dob": "",
        "ethnicity": "",
        "sex": "",
        "race": "",
        "zipCode": "",
        "ptStatus": "",
        "researchOptout": "",
    }

    problem_fields = {
        "ptMrn": "",
        "probId": "",
        "probDiagnosis": "",
        "probDesc": "",
        "probNotedDttm": "",
        "probResolvedDttm": "",
        "probStatus": "",
        "probComment": "",
    }

    history_fields = {
        "ptMrn": "",
        "encId": "",
        "hxContactDttm": "",
        "smokingQuitDttm": "",
        "smokingStartDttm": "",
        "smokePpd": "",
        "smokeYrs": "",
        "smokeTobUse": "",
        "smokelessTobUse": "",
        "smokeComment": "",
    }
