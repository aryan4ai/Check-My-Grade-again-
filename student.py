import csv

FILE = "data/students.csv"
FIELDS = ["email_address", "first_name", "last_name", "course_id", "grade", "marks"]

class Student:
    def __init__(self, email, first, last, course_id, grade, marks):
        self.email_address = email
        self.first_name = first
        self.last_name = last
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def display_records(self):
        with open(FILE, "r") as f:
            print(f.read())

    def add_new_student(self):
        with open(FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writerow({
                "email_address": self.email_address,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "course_id": self.course_id,
                "grade": self.grade,
                "marks": self.marks
            })
        print(f"Student {self.email_address} added.")

    def delete_student(self, email):
        rows = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            rows = [r for r in reader if r["email_address"] != email]
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Student {email} deleted.")

    def update_student_record(self, email, field, value):
        rows = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email_address"] == email:
                    row[field] = value
                rows.append(row)
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Student {email} updated.")

    def check_my_grades(self, email):
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email_address"] == email:
                    print(f"Grade: {row['grade']} | Marks: {row['marks']}")

    def check_my_marks(self, email):
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email_address"] == email:
                    print(f"Marks: {row['marks']}")