import os
import json
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import numpy as np

DATA_FILE = "menstrual_follow_up.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"menstrual_dates": [], "personal_notes": []}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def calculate_fertility_level(start_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    levels = []

    middle_start = start + timedelta(days=5)
    middle_finish = start + timedelta(days=12)
    levels.append({"Level": "Middle", "Start": middle_start.strftime("%Y-%m-%d"), "Finish": middle_finish.strftime("%Y-%m-%d")})

    high_start = middle_finish + timedelta(days=1)
    levels.append({"Level": "High", "Start": high_start.strftime("%Y-%m-%d"), "Finish": high_start.strftime("%Y-%m-%d")})

    weak_start = start + timedelta(days=14)
    weak_finish = start + timedelta(days=28)
    levels.append({"Level": "Weak", "Start": weak_start.strftime("%Y-%m-%d"), "Finish": weak_finish.strftime("%Y-%m-%d")})

    return levels

def add_menstrual_automatic(starts):
    start_date = datetime.strptime(starts, "%Y-%m-%d")
    finish_date = start_date + timedelta(days=4)

    fertility_levels = calculate_fertility_level(starts)

    data = load_data()
    data["menstrual_dates"].append({
        "Start": starts,
        "Finish": finish_date.strftime("%Y-%m-%d"),
        "Fertility Levels": fertility_levels
    })
    save_data(data)

def save():
    starts = starts_entry.get()
    try:
        add_menstrual_automatic(starts)
        messagebox.showinfo("Success", f"Period start date {starts} recorded successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter the date in the format 'YYYY-MM-DD'.")

def show():
    date_list = load_data()["menstrual_dates"]
    if not date_list:
        messagebox.showinfo("Info", "No menstrual data recorded yet!")
        return

    message_ = ""
    for entry in date_list:
        message_ += f"Start: {entry['Start']}, Finish: {entry['Finish']}\n"
        message_ += "Fertility Levels:\n"
        for level in entry["Fertility Levels"]:
            message_ += f"  {level['Level']}: {level['Start']} - {level['Finish']}\n"
        message_ += "\n"
    messagebox.showinfo("Menstrual and Fertility Information", message_)

root = tk.Tk()
root.title("Menstrual Follow Up and Fertility Levels")

tk.Label(root, text="Start Date (YYYY-MM-DD):").pack()
starts_entry = tk.Entry(root)
starts_entry.pack()

tk.Button(root, text="Save", command=save).pack()
tk.Button(root, text="Show Menstrual and Fertility Information", command=show).pack()

def add_personal_note():
    date = note_date_entry.get()
    note = note_entry.get()
    try:
        datetime.strptime(date, "%Y-%m-%d")
        data = load_data()
        data["personal_notes"].append({"Date": date, "Note": note})
        save_data(data)
        messagebox.showinfo("Success", "Note added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date in the format 'YYYY-MM-DD'.")

tk.Label(root, text="Date for Note (YYYY-MM-DD):").pack()
note_date_entry = tk.Entry(root)
note_date_entry.pack()

tk.Label(root, text="Personal Note:").pack()
note_entry = tk.Entry(root)
note_entry.pack()

tk.Button(root, text="Add Note", command=add_personal_note).pack()

def generate_hormone_levels(start_date):
    days = np.arange(1, 29).tolist()
    fsh = [5 + (i if i < 14 else 28 - i) * 0.5 for i in range(28)]
    lh = [2 + (0 if i < 12 else (i - 12) * 2) if i <= 14 else 30 - (i - 14) * 2 for i in range(28)]
    estrogen = [50 + (i if i < 14 else 28 - i) * 5 for i in range(28)]
    progesterone = [1 if i < 14 else (i - 14) * 2 for i in range(28)]

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    date_list = [start_date + timedelta(days=i - 1) for i in days]
    return date_list, fsh, lh, estrogen, progesterone

def plot_hormone_levels():
    data = load_data()
    if not data["menstrual_dates"]:
        messagebox.showerror("Error", "No menstrual data found! Please record a start date first.")
        return

    start_date = data["menstrual_dates"][-1]["Start"]
    date_list, fsh, lh, estrogen, progesterone = generate_hormone_levels(start_date)

    plt.figure(figsize=(12, 6))
    plt.plot(date_list, fsh, label="FSH", color="blue", linewidth=2)
    plt.plot(date_list, lh, label="LH", color="green", linewidth=2)
    plt.plot(date_list, estrogen, label="Estrogen", color="purple", linewidth=2)
    plt.plot(date_list, progesterone, label="Progesterone", color="orange", linewidth=2)

    plt.title("Hormone Levels During the Menstrual Cycle")
    plt.xlabel("Date")
    plt.ylabel("Hormone Levels (Unit)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

tk.Button(root, text="Show Hormone Levels Graph", command=plot_hormone_levels).pack()

root.mainloop()
