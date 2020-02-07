import json

in_file = open("patient_data.txt", "r")
new_patient = json.load(in_file)
in_file.close()
print(new_patient)