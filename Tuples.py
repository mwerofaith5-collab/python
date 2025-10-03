
patient = ("Mary via", 45, "120/80", 72)
print("Age:", patient[1])
print("Heart Rate:", patient[3])
patient_list = list(patient)
patient_list[3] = 75 
updated_patient = tuple(patient_list)
patients = (
    ("Kelse", 30, "110/70", 68),
    ("viola", 55, "130/85", 72),
    ("Brayo", 40, "120/80", 70),
    ("Ochola", 65, "140/90", 75),
    ("lin", 50, "125/78", 69)
)
names = [p[0] for p in patients]
print("Updated patient record:", updated_patient)
print("Patient names:", names)