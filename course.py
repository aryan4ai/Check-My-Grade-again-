import csv

FILE = "data/courses.csv"
FIELDS = ["course_id", "course_name", "description"]

class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.course_name = name
        self.description = description

    def display_courses(self):
        with open(FILE, "r") as f:
            print(f.read())

    def add_new_course(self):
        with open(FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writerow({
                "course_id": self.course_id,
                "course_name": self.course_name,
                "description": self.description
            })
        print(f"Course {self.course_id} added.")

    def delete_new_course(self, course_id):
        rows = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            rows = [r for r in reader if r["course_id"] != course_id]
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Course {course_id} deleted.")