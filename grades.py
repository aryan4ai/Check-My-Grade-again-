import csv
import statistics

FILE = "data/students.csv"

class Grades:
    GRADE_MAP = {
        "A": (90, 100),
        "B": (80, 89),
        "C": (70, 79),
        "D": (60, 69),
        "F": (0, 59)
    }

    def display_grade_report(self, course_id=None):
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if course_id is None or row["course_id"] == course_id:
                    print(row)

    def add_grade(self, email, grade, marks):
        rows = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                if row["email_address"] == email:
                    row["grade"] = grade
                    row["marks"] = marks
                rows.append(row)
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def delete_grade(self, email):
        self.add_grade(email, "", "")

    def modify_grade(self, email, new_grade, new_marks):
        self.add_grade(email, new_grade, new_marks)

    def average_marks(self, course_id):
        marks = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["course_id"] == course_id and row["marks"]:
                    marks.append(float(row["marks"]))
        if marks:
            print(f"Average: {sum(marks)/len(marks):.2f}")
        return marks

    def median_marks(self, course_id):
        marks = self.average_marks(course_id)
        if marks:
            print(f"Median: {statistics.median(marks):.2f}")