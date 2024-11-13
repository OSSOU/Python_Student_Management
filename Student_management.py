import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the file path for storing student data
FILE_PATH = "student_data.json"

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # Dictionary of subjects and marks

    def calculate_grade(self):
        try:
            total_marks = sum(self.marks.values())
            num_subjects = len(self.marks)
            average = total_marks / num_subjects
            if average >= 90:
                return 'A'
            elif average >= 80:
                return 'B'
            elif average >= 70:
                return 'C'
            elif average >= 60:
                return 'D'
            else:
                return 'F'
        except ZeroDivisionError:
            return "N/A"

class StudentGradeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Management System")
        self.students = self.load_students()

        # Tkinter Variables
        self.name_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.marks_var = tk.StringVar()

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Student Grade Management System", font=("Arial", 16))
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Name Entry
        tk.Label(self.root, text="Name:").grid(row=1, column=0, sticky='e')
        tk.Entry(self.root, textvariable=self.name_var).grid(row=1, column=1)

        # Roll Number Entry
        tk.Label(self.root, text="Roll Number:").grid(row=2, column=0, sticky='e')
        tk.Entry(self.root, textvariable=self.roll_var).grid(row=2, column=1)

        # Marks Entry
        tk.Label(self.root, text="Marks (Subject:Mark, e.g., Math:85):").grid(row=3, column=0, sticky='e')
        tk.Entry(self.root, textvariable=self.marks_var).grid(row=3, column=1)

        # Buttons
        tk.Button(self.root, text="Add Student", command=self.add_student).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="View Students", command=self.view_students).grid(row=4, column=1, pady=10)

    def add_student(self):
        name = self.name_var.get().strip()
        roll_number = self.roll_var.get().strip()
        marks_input = self.marks_var.get().strip()

        if not name or not roll_number or not marks_input:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        try:
            marks = dict(item.split(":") for item in marks_input.split(","))
            marks = {subject.strip(): float(mark.strip()) for subject, mark in marks.items()}
            student = Student(name, roll_number, marks)
            self.students[roll_number] = student.__dict__
            self.save_students()
            messagebox.showinfo("Success", f"Student {name} added successfully.")
        except ValueError:
            messagebox.showerror("Input Error", "Marks format is invalid!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_students(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")

        row = 0
        for roll_number, student_data in self.students.items():
            student = Student(**student_data)
            grade = student.calculate_grade()
            tk.Label(view_window, text=f"Name: {student.name}").grid(row=row, column=0, sticky='w')
            tk.Label(view_window, text=f"Roll Number: {student.roll_number}").grid(row=row, column=1, sticky='w')
            tk.Label(view_window, text=f"Marks: {student.marks}").grid(row=row, column=2, sticky='w')
            tk.Label(view_window, text=f"Grade: {grade}").grid(row=row, column=3, sticky='w')
            row += 1

    def load_students(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                return json.load(file)
        return {}

    def save_students(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.students, file, indent=4)

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGradeManager(root)
    root.mainloop()
