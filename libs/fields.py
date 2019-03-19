#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This Module Stores Field Mapping"""


class UhHospital(object):
    """Field Maps for UH Hospital"""

    PATIENT_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "PT_LAST_NAME": "",
        "PT_FIRST_NAME": "",
        "PT_MIDDLE_NAME": "",
        "PT_BIRTH_DTTM": "",
        "PT_ETHNICITY": "",
        "PT_SEX": "",
        "PT_RACE": "",
        "PT_ZIP": "",
        "PT_DEATH_DTTM": "",
        "PT_STATUS": "",
        "PT_WEIGHT": "",
        "PT_HEIGHT": "",
    }

    ALLERGY_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "ALLERGY_ALRGN": "",
        "ALLERGY_ALRGN_TYPE": "",
        "ALLERGY_TYPE": "",
        "ALLERGY_RXN": "",
        "ALLERGY_SVRTY_LEVEL": "",
        "ALLERGY_RXN_COMMENT": "",
        "ALLERGY_ENTERED_DTTM": "",
        "ALLERGY_ID": "",
        "ALLERGY_CATEGORY": "",
        "ALLERGY_STATUS": "",
    }

    AMBULATORY_IMAGING_REPORT_FEILDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "ORD_ID": "",
        "ORD_MD": "",
        "AUTH_MD," "FINAL_MD": "",
        "DICTATE_MD": "",
        "IMG_COLLECTION_DTTM": "",
        "IMG_RESLT_DTTM": "",
        "ADDEND_NOTE_ID": "",
        "ADDEND_DTTM": "",
        "IMG_RSLT_TEXT": "",
        "ADDEND_RSLT_TEXT": "",
        "ENC_ID": "",
    }

    AMBULATORY_MEDICATION_REPORT_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "ORD_ID": "",
        "ORD_MD": "",
        "AUTH_MD," "FINAL_MD": "",
        "DICTATE_MD": "",
        "IMG_COLLECTION_DTTM": "",
        "IMG_RESLT_DTTM": "",
        "ADDEND_NOTE_ID": "",
        "ADDEND_DTTM": "",
        "IMG_RSLT_TEXT": "",
        "ADDEND_RSLT_TEXT": "",
        "ENC_ID": "",
    }

    AP_REPORT_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "AP_ORDER_ID": "",
        "AP_ORDER_STS_CD": "",
        "RESULT_DTTM": "",
        "COLLECTION_DTTM": "",
        "SPECIMEN_SRC_LIST": "",
        "ORD_MD": "",
        "RESULT_MD": "",
        "RESULT_TEXT": "",
        "ENC_ID": "",
    }

    ENCOUNTERS_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "ENC_ID": "",
        "ENC_ADMIT_DTTM": "",
        "ENC_DISCHARGE_DTTM": "",
        "ADMIT_MD": "",
        "ATND_MD": "",
        "REFER_MD": "",
        "PCP_MD": "",
        "CONSULT_MD": "",
        "ENC_MAJOR_TYPE": "",
        "ENC_PATIENT_CLASS": "",
        "ENC_ADMIT_SOURCE": "",
        "ENC_STATUS_1": "",
        "ENC_STATUS_2": "",
        "ENC_ADMISSION_TYPE": "",
        "ER_COMPLAINT": "",
        "ENC_DX": "",
        "ADMIT_DX": "",
        "ADMIT_DX_TEXT": "",
    }

    IMAGING_REPORT_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "ORD_ID": "",
        "ORD_MD": "",
        "AUTH_MD": "",
        "FINAL_MD": "",
        "DICTATE_MD": "",
        "IMG_COLLECTION_DTTM": "",
        "IMG_RESLT_DTTM": "",
        "ADDEND_NOTE_ID": "",
        "ADDEND_DTTM": "",
        "IMG_RESLT_TEXT": "",
        "ADDEND_RESLT_TEXT": "",
        "ENC_ID": "",
    }

    LAB_REPORT_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "LAB_ORDER_ID": "",
        "LAB_LINE_NO": "",
        "LAB_LOINC": "",
        "LAB_PROCEDURE": "",
        "LAB_RSLT_COLLECTION_DTTM": "",
        "LAB_RSLT_DTTM": "",
        "LAB_RSLT_VALUE": "",
        "LAB_RSLT_UOM": "",
        "LAB_DATA_TYPE": "",
        "RESULTING_LAB": "",
        "LAB_PROC_COMMENTS": "",
        "LAB_TEST_COMMENT": "",
        "ENC_ID": "",
    }

    MEDICATION_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "ORD_ID": "",
        "ORD_MED_START_DTTM": "",
        "ORD_MED_END_DTTM": "",
        "ORD_MED_FREQUENCY": "",
        "ORD_MED_NO_OF_DOSES": "",
        "ORD_MED_NM": "",
        "ORD_MED_RXNORM": "",
        "ORD_MED_AMT_MIN": "",
        "ORD_MED_AMT_MAX": "",
        "ORD_MED_UNITS": "",
        "ORD_MED_ORDERING_PROV": "",
        "ORD_MED_VERIFYING_PROV": "",
        "ORD_MED_ADMIN_INSTRUCTIONS": "",
        "ORD_MED_PRN_REASONS": "",
        "ENC_ID": "",
    }

    NOTES_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "NOTE_ID": "",
        "ENC_MAJOR_TYPE": "",
        "NOTE_DOS": "",
        "NOTE_TYPE": "",
        "NOTE_CREATE_PROV": "",
        "NOTE_SIGN_PROV": "",
        "NOTE_FIRST_SIGN_DTTM": "",
        "NOTE_CURRENT_AUTH": "",
        "NOTE_TEXT": "",
        "ENC_ID": "",
    }
    PROBLEM_FIELDS = {
        "SITE_ID": "",
        "PT_MRN": "",
        "PROB_ID": "",
        "PROB_DIAGNOSIS": "",
        "PROB_DESC": "",
        "PROB_ICD_LIST": "",
        "PROB_NOTED_DTTM": "",
        "PROB_RESOLVED_DTM": "",
        "PROB_STATUS": "",
        "PROB_COMMENT": "",
        "ENC_ID": "",
    }

    PROVIDER_FIELDS = {
        "SITE_ID",
        "IDENTITY_ID",
        "PROV_LAST_NAME",
        "PROV_FIRST_NAME",
        "SPECIALTY",
        "PHONE",
        "EMAIL",
        "PROVIDER_TYPE",
        "ADDR_LINE_1",
        "ADDR_LINE_2",
        "ADDR_LINE_3",
        "CITY",
        "STATE",
        "ZIP",
    }
    SITE_FIELDS = {
        "SITE_ID": "",
        "SITE_NAME": "",
        "PHONE": "",
        "EMAIL": "",
        "ADDR_LINE_1": "",
        "ADDR_LINE_2": "",
        "ADDR_LINE_3": "",
        "CITY": "",
        "STATE": "",
        "ZIP": "",
        "URL": "",
    }
