#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Artifact Manager
"""
import uuid
import random
from faker import Faker
from libs.fields import UhHospital as uhf


class ArtifactManager(object):
    """Class to manage record creation"""
    def __init__(self, mrn):
        self.mrn = mrn
        self.fake = Faker()

    def generate_patient_record(self):
        """Generate Patient Record"""
        sex = ["M", "F"]
        random_sex = random.choice(sex)
        height = "{}'{} tall".format(random.randint(5, 6),
                                     random.randint(1, 10))
        weight = "{} kg".format(random.randint(40.0, 181.0))
        patient = uhf.patient_fields
        patient['PT_MRN'] = self.mrn
        patient['PT_LAST_NAME'] = self.fake.last_name()
        patient['PT_MIDDLE_NAME'] = self.fake.last_name()
        patient['PT_SEX'] = random_sex
        patient['PT_STATUS'] = "Alive"
        patient['PT_HEIGHT'] = height
        patient['PT_WEIGHT'] = weight
        patient['PT_BIRTH_DTTM'] = self.fake.iso8601()
        if random_sex == 'M':
            patient['PT_FIRST_NAME'] = self.fake.first_name_male()
        elif random_sex is 'F':
            patient['PT_FIRST_NAME'] = self.fake.first_name_female()

        return patient

    def generate_notes(self, note_seed):
        note = uhf.notes_fields
        note['PT_MRN'] = self.mrn
        note['NOTE_DOS'] = self.fake.iso8601()
        note['NOTE_TYPE'] = "Patient Profile - Adult"
        note['NOTE_TEXT'] = note_seed
        return note
