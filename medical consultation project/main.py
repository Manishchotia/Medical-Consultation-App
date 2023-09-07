import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Patient(User):
    def __init__(self, username, password, name, age):
        super().__init__(username, password)
        self.name = name
        self.age = age
        self.symptoms = []
        self.medical_history = []  # Add a medical_history attribute

class Doctor(User):
    def __init__(self, username, password, name, specialization):
        super().__init__(username, password)
        self.name = name
        self.specialization = specialization

class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

class MedicalConsultationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Consultation App")

        self.users = []  # Store user objects
        self.doctors = []  # Store doctor objects
        self.appointments = []  # Store appointment objects
        self.current_user = None

        self.login_frame = tk.Frame(root)
        self.patient_frame = tk.Frame(root)
        self.doctor_frame = tk.Frame(root)

        self.create_login_frame()
        self.create_patient_frame()
        self.create_doctor_frame()

        self.show_login_frame()

    def show_login_frame(self):
        self.login_frame.pack()
        self.patient_frame.pack_forget()
        self.doctor_frame.pack_forget()

    def show_patient_frame(self):
        self.login_frame.pack_forget()
        self.patient_frame.pack()
        self.doctor_frame.pack_forget()

    def show_doctor_frame(self):
        self.login_frame.pack_forget()
        self.patient_frame.pack_forget()
        self.doctor_frame.pack()

    def create_login_frame(self):
        label = tk.Label(self.login_frame, text="Login Menu", font=("Helvetica", 16))
        label.pack(pady=10)

        tk.Button(self.login_frame, text="Log in as a patient", command=self.login_patient).pack(pady=5)
        tk.Button(self.login_frame, text="Log in as a doctor", command=self.login_doctor).pack(pady=5)
        tk.Button(self.login_frame, text="Register as a patient", command=self.register_patient).pack(pady=5)
        tk.Button(self.login_frame, text="Register as a doctor", command=self.register_doctor).pack(pady=5)
        tk.Button(self.login_frame, text="Exit", command=self.root.destroy).pack(pady=5)

    def create_patient_frame(self):
        self.patient_frame = tk.Frame(self.root)

        label = tk.Label(self.patient_frame, text="Patient Menu", font=("Helvetica", 16))
        label.pack(pady=10)

        tk.Button(self.patient_frame, text="Consult a Doctor", command=self.consult_doctor).pack(pady=5)
        tk.Button(self.patient_frame, text="View Symptoms", command=self.view_symptoms).pack(pady=5)
        tk.Button(self.patient_frame, text="Schedule an Appointment", command=self.schedule_appointment).pack(pady=5)
        tk.Button(self.patient_frame, text="View Medical History", command=self.view_medical_history).pack(pady=5)
        tk.Button(self.patient_frame, text="Logout", command=self.logout).pack(pady=5)

    def create_doctor_frame(self):
        self.doctor_frame = tk.Frame(self.root)

        label = tk.Label(self.doctor_frame, text="Doctor Menu", font=("Helvetica", 16))
        label.pack(pady=10)

        tk.Button(self.doctor_frame, text="View Appointments", command=self.view_appointments).pack(pady=5)
        tk.Button(self.doctor_frame, text="View Patient Medical History", command=self.view_patient_medical_history).pack(pady=5)
        tk.Button(self.doctor_frame, text="Logout", command=self.logout).pack(pady=5)

    def login_patient(self):
        # Add your login logic here
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Placeholder logic, replace with actual user validation
        for user in self.users:
            if isinstance(user, Patient) and user.username == username and user.password == password:
                self.current_user = user
                self.show_patient_frame()
                return

        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def login_doctor(self):
        # Add your login logic here
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Placeholder logic, replace with actual user validation
        for user in self.users:
            if isinstance(user, Doctor) and user.username == username and user.password == password:
                self.current_user = user
                self.show_doctor_frame()
                return

        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def register_patient(self):
        # Add your registration logic here
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        # Placeholder logic, replace with actual user registration
        self.users.append(Patient(username, password, name, age))
        messagebox.showinfo("Registration", "Registration successful. You can now log in as a patient.")

    def register_doctor(self):
        # Add your registration logic here
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        name = input("Enter your name: ")
        specialization = input("Enter your specialization: ")

        # Placeholder logic, replace with actual user registration
        self.users.append(Doctor(username, password, name, specialization))
        self.doctors.append(Doctor(username, password, name, specialization))
        messagebox.showinfo("Registration", "Registration successful. You can now log in as a doctor.")

    def consult_doctor(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please log in to consult a doctor.")
            return

        if isinstance(self.current_user, Patient):
            print("Describe your symptoms:")
            symptoms = input("Symptoms: ")
            self.current_user.symptoms.append(symptoms)
            response = self.simulate_doctor_response(symptoms)
            print(f"Doctor's response: {response}")
        else:
            messagebox.showerror("Error", "Only patients can consult a doctor.")

    def view_symptoms(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please log in to view symptoms.")
            return

        if isinstance(self.current_user, Patient):
            symptoms = self.current_user.symptoms
            if symptoms:
                print("Your Symptoms:")
                for symptom in symptoms:
                    print(symptom)
            else:
                print("No symptoms recorded.")
        else:
            messagebox.showerror("Error", "Only patients can view their symptoms.")

    def simulate_doctor_response(self, symptoms):
        # This is a placeholder function for simulating a doctor's response
        if "fever" in symptoms:
            return "You may have a common cold. Rest and drink fluids."
        elif "headache" in symptoms:
            return "You may be experiencing a tension headache. Try relaxation techniques."
        else:
            return "Your symptoms are not specific. Please consult a healthcare professional for a proper diagnosis."

    def schedule_appointment(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please log in to schedule an appointment.")
            return

        if isinstance(self.current_user, Patient):
            print("Schedule an Appointment:")
            doctor_name = input("Enter doctor's name: ")
            date = input("Enter date (MM/DD/YYYY): ")
            time = input("Enter time: ")
            doctor = None

            # Find the doctor by name (you can replace this with your own logic)
            for doc in self.doctors:
                if doc.name == doctor_name:
                    doctor = doc
                    break

            if doctor:
                appointment = Appointment(doctor, self.current_user, date, time)
                self.appointments.append(appointment)
                print(f"Appointment scheduled with Dr. {doctor.name} on {date} at {time}.")
            else:
                print(f"Doctor with the name '{doctor_name}' not found.")
        else:
            messagebox.showerror("Error", "Only patients can schedule appointments.")

    def view_medical_history(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please log in to view medical history.")
            return

        if isinstance(self.current_user, Patient):
            medical_history = self.current_user.medical_history
            if medical_history:
                print("Medical History:")
                for entry in medical_history:
                    print(entry)
            else:
                print("No medical history available.")
        else:
            messagebox.showerror("Error", "Only patients can view their medical history.")

    def view_appointments(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please log in to view appointments.")
            return

        if isinstance(self.current_user, Doctor):
            appointments = [appointment for appointment in self.appointments if appointment.doctor == self.current_user]
            if appointments:
                print("Your Appointments:")
                for appointment in appointments:
                    print(f"Patient: {appointment.patient.name}, Date: {appointment.date}, Time: {appointment.time}")
            else:
                print("No appointments scheduled.")
        else:
            messagebox.showerror("Error", "Only doctors can view their appointments.")

    def view_patient_medical_history(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please log in to view patient medical history.")
            return

        if isinstance(self.current_user, Doctor):
            patient_name = input("Enter patient's name: ")
            patient = None

            # Find the patient by name (you can replace this with your own logic)
            for user in self.users:
                if isinstance(user, Patient) and user.name == patient_name:
                    patient = user
                    break

            if patient:
                medical_history = patient.medical_history
                if medical_history:
                    print(f"Medical History for {patient.name}:")
                    for entry in medical_history:
                        print(entry)
                else:
                    print(f"No medical history available for {patient.name}.")
            else:
                print(f"Patient with the name '{patient_name}' not found.")
        else:
            messagebox.showerror("Error", "Only doctors can view patient medical history.")

    def logout(self):
        self.current_user = None
        self.show_login_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalConsultationApp(root)
    root.mainloop()
