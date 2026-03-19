import csv

FILE = "data/professors.csv"
FIELDS = ["professor_id", "professor_name", "rank", "course_id"]

class Professor:
    def __init__(self, prof_id, name, rank, course_id):
        self.professor_id = prof_id
        self.professor_name = name
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        with open(FILE, "r") as f:
            print(f.read())

    def add_new_professor(self):
        with open(FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writerow({
                "professor_id": self.professor_id,
                "professor_name": self.professor_name,
                "rank": self.rank,
                "course_id": self.course_id
            })
        print(f"Professor {self.professor_id} added.")

    def delete_professor(self, prof_id):
        rows = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            rows = [r for r in reader if r["professor_id"] != prof_id]
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Professor {prof_id} deleted.")

    def modify_professor_details(self, prof_id, field, value):
        rows = []
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["professor_id"] == prof_id:
                    row[field] = value
                rows.append(row)
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def show_course_details_by_professor(self, prof_id):
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["professor_id"] == prof_id:
                    print(f"Course: {row['course_id']}")