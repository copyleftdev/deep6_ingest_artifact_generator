from libs.artifact_generator import ArtifactManager as am

a = am("444543356")
patient = a.generate_patient_record()
note = a.generate_notes("sample")
print(patient)
print(note)
