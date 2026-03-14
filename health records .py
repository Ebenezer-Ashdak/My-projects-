import tkinter as tk
from tkinter import messagebox
import datetime

# ==========================
# FUNCTION: SAVE RECORD
# ==========================

def save_record(report):
    with open("health_records.txt", "a") as file:
        file.write(report + "\n" + "-"*50 + "\n")

# ==========================
# FUNCTION: VIEW RECORDS
# ==========================

def view_records():
    try:
        with open("health_records.txt", "r") as file:
            data = file.read()
        messagebox.showinfo("Saved Records", data)
    except:
        messagebox.showinfo("Records", "No records found.")

# ==========================
# FUNCTION: HEALTH ASSESSMENT
# ==========================

def assess_health():
    name = name_entry.get()
    gender = gender_var.get()

    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert cm to meters
        bp = int(bp_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid numeric values.")
        return

    risk_score = 0

    # BMI Calculation
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        bmi_status = "Underweight"
        risk_score += 1
    elif 18.5 <= bmi < 25:
        bmi_status = "Normal"
    elif 25 <= bmi < 30:
        bmi_status = "Overweight"
        risk_score += 1
    else:
        bmi_status = "Obese"
        risk_score += 2

    # Blood Pressure Check
    if 90 <= bp <= 120:
        bp_status = "Normal"
    else:
        bp_status = "Abnormal"
        risk_score += 1

    # Final Risk Level
    if risk_score == 0:
        risk_level = "LOW RISK"
        advice = "Maintain healthy lifestyle."
    elif risk_score <= 2:
        risk_level = "MODERATE RISK"
        advice = "Improve diet and exercise regularly."
    else:
        risk_level = "HIGH RISK"
        advice = "Consult a healthcare professional."

    # Create Report
    now = datetime.datetime.now()
    report = f"""
Date: {now}
Patient: {name}
Age: {age}
Gender: {gender}

BMI: {bmi:.2f} ({bmi_status})
Blood Pressure: {bp_status}

Final Risk Level: {risk_level}
Advisory: {advice}
"""

    save_record(report)

    messagebox.showinfo("Health Report", report)

# ==========================
# GUI SETUP
# ==========================

root = tk.Tk()
root.title("Community Health Tracker Pro")
root.geometry("420x750")
root.configure(bg="#eef7ff")

title = tk.Label(root,
                 text="Community Health Tracker PRO",
                 font=("Arial", 16, "bold"),
                 bg="#eef7ff")
title.pack(pady=10)

# Patient Info
tk.Label(root, text="Patient Name:", bg="#eef7ff").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:", bg="#eef7ff").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender:", bg="#eef7ff").pack()
gender_var = tk.StringVar()
gender_menu = tk.OptionMenu(root, gender_var, "female", "male", "general")
gender_menu.pack()

# Health Data
tk.Label(root, text="Weight (kg):", bg="#eef7ff").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (cm):", bg="#eef7ff").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Blood Pressure (mmHg):", bg="#eef7ff").pack()
bp_entry = tk.Entry(root)
bp_entry.pack()

# Buttons
tk.Button(root,
          text="Assess Health",
          bg="green",
          fg="white",
          command=assess_health).pack(pady=10)

tk.Button(root,
          text="View Saved Records",
          bg="blue",
          fg="white",
          command=view_records).pack(pady=5)

root.mainloop()