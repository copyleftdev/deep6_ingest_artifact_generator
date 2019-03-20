"""
Mayo Model
"""


class Mayo(object):
    """Mayo Fields"""

    encounter_fields = {
        "patientMrn": "",
        "encounterId": "",
        "admitDate": "",
        "dischargeDate": "",
        "admittingMd": "",
        "attendingMd": "",
        "encounterMajorType": "",
        "encounterStatus1": "",
        "encounterStatus2": "",
        "encounterAdmissionType": "",
        "complaintText": "",
        "encounterDiagnosis": "",
        "admittingDiagnosis": "",
        "admittingDiagnosisText": "",
    }

    genetics_report_fields = {
        "patientMrn": "",
        "reportDate": "",
        "reportId": "",
        "reportText": "",
        "geneCodes": "",
    }

    imaging_report_fields = {
        "patientMrn": "",
        "orderId": "",
        "collectionDate": "",
        "resultDate": "",
        "imgResultText": "",
    }

    lab_report_fields = {
        "patientMrn": "",
        "orderId": "",
        "labProcedure": "",
        "resultCollectionDate": "",
        "resultDate": "",
        "resultValue": "",
        "resultMeasurementUnit": "",
        "dataType": "",
    }

    medication_order_fields = {
        "patientMrn": "",
        "orderId": "",
        "orderDate": "",
        "startDate": "",
        "endDate": "",
        "medicationName": "",
        "numDoses": "",
        "dosageUnits": "",
        "frequency": "",
        "medAmount": "",
        "medicationStrength": "",
        "medicationStrengthUnits": "",
    }

    pathology_report_fields = {
        "patientMrn": "",
        "orderId": "",
        "resultDate": "",
        "resultText": "",
        "collectionDate": "",
    }

    patient_fields = {
        "patientMrn": "",
        "birthDate": "",
        "age": "",
        "firstName": "",
        "lastName": "",
        "middleName": "",
        "ethnicity": "",
        "races": "",
        "gender": "",
    }

    physician_note_fields = {
        "patientMrn": "",
        "noteId": "",
        "dateOfService": "",
        "text": "",
    }

    post_ops_notes = {
        "patientMrn": "",
        "noteId": "",
        "dateOfService": "",
        "icd9Codes": "",
        "icd10Codes": "",
        "orderingMd": "",
        "authorizingMd": "",
        "performingMds": "",
        "noteText": "",
    }

    problem_list_fields = {
        "patientMrn": "",
        "problemID": "",
        "problemDiagnosisCode": "",
        "problemDescription": "",
        "dateProblemNoted": "",
        "problemStatus": "",
    }

    provider_details = {
        "patientMrn": "",
        "problemID": "",
        "problemDiagnosisCode": "",
        "problemDescription": "",
        "dateProblemNoted": "",
        "problemStatus": "",
    }
