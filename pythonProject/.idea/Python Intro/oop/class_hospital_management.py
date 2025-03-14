class Patient:
    def __init__(self, name, patient_id, age, gender, medical_records):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.medical_records = medical_records


class Doctor:
    def __init__(self, doctor_name, specialty):
        self.doctor_name = doctor_name
        self.specialty = specialty


class Appointment:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def register_patients(self, name, patient_id, age, gender, medical_records):
        patient = Patient(name, patient_id, age, gender, medical_records)
        self.patients.append(patient)
        print(f"{name} registered successfully!")

    def add_doctor(self, doctor_name, specialty):
        doctor = Doctor(doctor_name, specialty)
        self.doctors.append(doctor)
        return self.doctors

    def scheduling_appointments(self, doctor, date, time):
        appointment = [doctor, date, time]
        if appointment not in self.appointments:
            self.appointments.append(appointment)
            print(f"Your Appointment for {doctor} is scheduled on {date} at {time}")
        else:
            print("Unavailable to schedule an appointment! Please change the date/time.")

    def access_medical_records(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                record = patient.medical_records
                print(f"Medical records for {patient_name} are: {record}")
                return
        print("No records available")


if __name__ == "__main__":
    appointment = Appointment()

    appointment.register_patients("Patient1", "P001", 23, "Female", "TTTS")
    appointment.register_patients("Patient2", "P002", 35, "Male", "GSW in the head")
    appointment.register_patients("Patient3", "P003", 11, "Female", "Cardiac arrest")
    appointment.register_patients("Patient4", "P004", 26, "Female", "Aneurysm in the Aortic Valve")

    appointment.add_doctor("Christina Yang", "Cardiologist")
    appointment.add_doctor("Derek Shephard", "Neurosurgeon")
    appointment.add_doctor("Addison Montgomery", "OB/GYN")

    appointment.scheduling_appointments("Addison Montgomery", "31-08-2024", "11:00")
    appointment.scheduling_appointments("Addison Montgomery", "31-08-2024", "11:00")
    appointment.scheduling_appointments("Cristina Yang", "31-08-2024", "11:00")

    appointment.access_medical_records("Patient1")
    appointment.access_medical_records("Patient4")
    appointment.access_medical_records("Patient01")

