# attendence_system
Student Attendance Management System

Overview

The Student Attendance Management System is a Python-based application designed to efficiently track and manage student attendance. Using a CSV file as a backend database, the system allows teachers or administrators to record, view, and update attendance easily. This project is ideal for small to medium-sized classes and is perfect for learning Python file handling and basic data management.

Features

Add New Students – Register new students in the system.

Mark Attendance – Record attendance for students on a given date.

View Attendance – Check attendance records for individual students.

Update Attendance – Modify attendance records if mistakes occur.

CSV Storage – Data is stored in a CSV file for easy access and portability.

User-Friendly Interface – Simple command-line interface for quick operations.

Prerequisites

Python 3.x installed on your system

Basic knowledge of Python programming

CSV module (built-in with Python)

Optional: pandas library for advanced operations

File Structure
Student Attendance System/
│
├── attendance.csv       # CSV file storing attendance records
├── students.csv         # CSV file storing student details
├── attendence_system.py             # Main Python script for the system
├── README.md            # Project documentation

How to Use
1. Run the Program
python attendence_system.py

2. Menu Options

Upon running, the program provides a menu like:

1. Add New Student
2. Mark Attendance
3. View Attendance
4. Update Attendance
5. Exit


Add New Student: Enter student ID, name, and class details.

Mark Attendance:  mark each student as Present (P) or Absent (A).

View Attendance: Display attendance records of a student.

Update Attendance: Correct any mistakes in the attendance records.

Exit: Close the program safely.

Sample CSV Format
students.csv
Student_ID	Name	Class
101	John Doe	10-A
102	Jane Smith	10-B
attendance.csv
Date	Student_ID	Status
2025-11-22	101	P
2025-11-22	102	A

Benefits

Easy to manage attendance for small classrooms.

Lightweight system using CSV; no heavy database required.

Can be extended to include email notifications or analytics.

Helps students and teachers maintain accurate attendance records.

Future Enhancements

GUI implementation using Tkinter or PyQt.

Generate attendance reports and charts.

Send automatic email notifications to absent students.

Integrate with databases like SQLite or MySQL.

Author

Name: Nimish Yadav
Email: 25BAI11011
GitHub: [Your GitHub Link]
