# GYEDU NHYIRAH EMMANUEL
# SCIENCE 2A
# COMPUTING PROJECT
# HOSPITAL QUEUE MANAGEMENT SYSTEM (IMPROVED GUI)

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

FILE_NAME = "patients.cDB"


# ---------------- LOGIC CLASS ----------------
class HospitalQueue:
    def __init__(self):
        self.patients = []

    def get_priority(self, condition):
        priorities = {
            "Critical": 1,
            "Emergency": 2,
            "Urgent": 3,
            "Serious": 4,
            "Stable": 5
        }
        return priorities.get(condition, 6)

    def add_patient(self, name, condition):
        patient = {
            "name": name,
            "condition": condition,
            "priority": self.get_priority(condition),
            "time": datetime.now()
        }
        self.patients.append(patient)
        self.save_to_file()

    def attend_patient(self):
        if not self.patients:
            return None
        self.patients.sort(key=lambda p: (p["priority"], p["time"]))
        patient = self.patients.pop(0)
        self.save_to_file()
        return patient

    def save_to_file(self):
        with open(FILE_NAME, "w") as file:
            for p in self.patients:
                file.write(f"{p['name']},{p['condition']},{p['priority']},{p['time']}\n")

    def load_from_file(self):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    name, condition, priority, time = line.strip().split(",")
                    self.patients.append({
                        "name": name,
                        "condition": condition,
                        "priority": int(priority),
                        "time": datetime.fromisoformat(time)
                    })
        except FileNotFoundError:
            pass


# ---------------- GUI FUNCTIONS ----------------
def refresh_list():
    listbox.delete(0, tk.END)
    hospital.patients.sort(key=lambda p: (p["priority"], p["time"]))
    for p in hospital.patients:
        listbox.insert(
            tk.END,
            f"{p['name']}  |  {p['condition']}"
        )
    status_label.config(text=f"Total patients: {len(hospital.patients)}")


def add_patient_gui():
    name = name_entry.get().strip()
    condition = condition_combo.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter patient name")
        return

    hospital.add_patient(name, condition)
    name_entry.delete(0, tk.END)
    refresh_list()
    status_label.config(text="Patient added successfully")


def attend_patient_gui():
    patient = hospital.attend_patient()
    if patient:
        messagebox.showinfo(
            "Now Attending",
            f"Patient Name: {patient['name']}\nCondition: {patient['condition']}"
        )
        refresh_list()
    else:
        messagebox.showinfo("Queue Empty", "No patients in the queue")


# ---------------- MAIN WINDOW ----------------
hospital = HospitalQueue()
hospital.load_from_file()

root = tk.Tk()
root.title("Hospital Queue Management System")
root.geometry("600x520")
root.configure(bg="#f4f6f7")

# ---------------- HEADER ----------------
header = tk.Frame(root, bg="#2c3e50", height=60)
header.pack(fill="x")

tk.Label(
    header,
    text="HOSPITAL PATIENT QUEUE MANAGEMENT SYSTEM",
    bg="#2c3e50",
    fg="white",
    font=("Arial", 14, "bold")
).pack(pady=15)

# ---------------- FORM SECTION ----------------
form_frame = tk.LabelFrame(
    root,
    text="Patient Information",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=15,
    bg="#f4f6f7"
)
form_frame.pack(fill="x", padx=20, pady=10)

form_frame.columnconfigure(1, weight=1)

tk.Label(form_frame, text="Patient Name:", bg="#f4f6f7").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, sticky="ew", pady=5)

tk.Label(form_frame, text="Condition:", bg="#f4f6f7").grid(row=1, column=0, sticky="w")

condition_combo = ttk.Combobox(
    form_frame,
    values=["Critical", "Emergency", "Urgent", "Serious", "Stable"],
    state="readonly"
)
condition_combo.current(4)
condition_combo.grid(row=1, column=1, sticky="ew", pady=5)

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root, bg="#f4f6f7")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Add Patient",
    width=15,
    bg="#27ae60",
    fg="white",
    command=add_patient_gui
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Attend Patient",
    width=15,
    bg="#e67e22",
    fg="white",
    command=attend_patient_gui
).grid(row=0, column=1, padx=10)

# ---------------- LIST SECTION ----------------
list_frame = tk.LabelFrame(
    root,
    text="Waiting Queue",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=10
)
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

listbox = tk.Listbox(
    list_frame,
    font=("Arial", 10),
    activestyle="none"
)
listbox.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(list_frame, command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)

# ---------------- STATUS BAR ----------------
status_label = tk.Label(
    root,
    text="System ready",
    anchor="w",
    bg="#dcdde1",
    padx=10
)
status_label.pack(fill="x")

refresh_list()
root.mainloop()