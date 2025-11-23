import csv
import os
from datetime import datetime

# ---------- FILE CHECK ----------
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerow(["roll", "name"])

if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w", newline="") as f:
        csv.writer(f).writerow(["date", "roll", "status"])


# ---------- FUNCTION : ADD STUDENT ----------
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    with open("students.csv", "a", newline="") as f:
        csv.writer(f).writerow([roll, name])

    print("Student added successfully!")


# ---------- FUNCTION : MARK ATTENDANCE ----------
def mark_attendance():
    today = datetime.now().strftime("%Y-%m-%d")

    print(f"\nMarking attendance for: {today}\n")

    with open("students.csv") as f:
        students = list(csv.DictReader(f))

    with open("attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)

        for stu in students:
            status = input(f"{stu['roll']} - {stu['name']} (P/A): ").upper()
            if status not in ['P', 'A']:
                status = 'A'
            writer.writerow([today, stu["roll"], status])

    print("\nAttendance saved!\n")


# ---------- FUNCTION : VIEW REPORT ----------
def view_report():
    roll = input("Enter Roll Number: ")

    total = present = 0

    with open("attendance.csv") as f:
        for row in csv.DictReader(f):
            if row["roll"] == roll:
                total += 1
                if row["status"] == "P":
                    present += 1

    if total == 0:
        print("No attendance available!")
        return

    percentage = (present / total) * 100

    print(f"\nTotal Classes: {total}")
    print(f"Present: {present}")
    print(f"Attendance %: {percentage:.2f}\n")


# ---------- MAIN MENU ----------
while True:
    print("=== Attendance Management System ===")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        mark_attendance()
    elif ch == "3":
        view_report()
    elif ch == "4":
        break
    else:
        print("Invalid option!")
