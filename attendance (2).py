import csv
import os
from datetime import datetime

STUDENTS_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"

def initialize_files():
    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["roll_number", "name", "branch"])

    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["roll_number", "name", "date", "status"])

def add_student(roll_number, name, branch):
    with open(STUDENTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll_number, name, branch])
    print(f"Student {name} added successfully.")

def get_all_students():
    students = []
    with open(STUDENTS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)
    return students

def mark_attendance(roll_number, status="Present"):
    students = get_all_students()
    student = next((s for s in students if s["roll_number"] == roll_number), None)

    if not student:
        print(f"Student with roll number {roll_number} not found.")
        return

    date_today = datetime.now().strftime("%Y-%m-%d")

    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll_number, student["name"], date_today, status])

    print(f"Attendance marked for {student['name']} - {status} on {date_today}")

def view_attendance_report():
    print("\n--- Attendance Report ---")
    print(f"{'Roll No':<15} {'Name':<25} {'Date':<15} {'Status':<10}")
    print("-" * 65)
    with open(ATTENDANCE_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['roll_number']:<15} {row['name']:<25} {row['date']:<15} {row['status']:<10}")

def calculate_attendance_percentage(roll_number):
    total = 0
    present = 0
    with open(ATTENDANCE_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["roll_number"] == roll_number:
                total += 1
                if row["status"] == "Present":
                    present += 1

    if total == 0:
        print("No attendance records found.")
        return

    percentage = (present / total) * 100
    print(f"\nAttendance for Roll No {roll_number}:")
    print(f"Total Classes: {total}")
    print(f"Present: {present}")
    print(f"Attendance Percentage: {percentage:.2f}%")

def main():
    initialize_files()

    while True:
        print("\n=== Student Attendance Management System ===")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Report")
        print("4. Check Attendance Percentage")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            roll = input("Enter Roll Number: ").strip()
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch: ").strip()
            add_student(roll, name, branch)

        elif choice == "2":
            roll = input("Enter Roll Number: ").strip()
            status = input("Enter Status (Present/Absent): ").strip()
            mark_attendance(roll, status)

        elif choice == "3":
            view_attendance_report()

        elif choice == "4":
            roll = input("Enter Roll Number: ").strip()
            calculate_attendance_percentage(roll)

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
