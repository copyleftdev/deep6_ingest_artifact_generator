import json


class MimicJson(object):
    def patient_obj(self):
        races = []
        patient = {
            "birthDate": "",
            "deathDate": "",
            "email": "",
            "ethnicity": "",
            "firstName": "",
            "gender": "",
            "hasResearchOptOut": "",
            "height": "",
            "isConfidential": "",
            "lastName": "",
            "maritalStatus": "",
            "middleName": "",
            "mortalityStatus": "",
            "mrn": "",
            "phoneNumberCell": "",
            "phoneNumberHome": "",
            "phoneNumberWork": "",
            "races": races,
            "uuid": "",
            "weight": "",
            "zip": "",
        }
        d6_analysed_data_element = []
        d6_analysed_data_codes = []
        d6_analysed_freetext_phrases = []
        d6_analysed = {
            "dataElements": d6_analysed_data_element,
            "codes": d6_analysed_data_codes,
            "freeTextPhrases": d6_analysed_freetext_phrases,
        }

        agents = []
        entities = []
        activities = []
        derivations = []
        attrbutions = []
        generations = []
        provenance = {
            "eventId": "",
            "agents": agents,
            "entities": entities,
            "activities": activities,
            "derivations": derivations,
            "attrbutions": attrbutions,
            "generations": generations,
        }
        metadata = {"batchid": "", "provenance": provenance}
        schema = {"name": "Patient", "parent": ""}

        content_codes = []
        contents = {
            "codes": content_codes,
            "type": "",
            "value": "",
            "annotatableForNLP": "",
            "freeTextSearchable": "",
        }
        provider = {
            "id": "",
            "lasName": "",
            "firstName": "",
            "middlename": "",
            "fullName": "",
            "title": "",
            "role": "",
        }
        providers = []
        contents = []
        encouterids = []
        event = {"providers":providers, "contents": contents,"encounterIds": encouterids, "episodeItem": "episodeItem" }
        root = {
            "ProviderDetails": "",
            "event": "",
            "patient": patient,
            "d6Analyzed": d6_analysed,
            "metadata": metadata,
            "schema": schema,
            "event" : event,
        }
        return root


a = MimicJson()
a.notes()
