import csv
import time

def load_students():
    with open("data/students.csv", "r") as f:
        return list(csv.DictReader(f))

def search_student(email):
    start = time.time()
    students = load_students()
    result = [s for s in students if s["email_address"] == email]
    elapsed = time.time() - start
    print(f"Search completed in {elapsed:.6f} seconds")
    return result

def sort_students(key="marks", reverse=False):
    start = time.time()
    students = load_students()
    sorted_students = sorted(
        students,
        key=lambda x: float(x[key]) if key == "marks" else x[key],
        reverse=reverse
    )
    elapsed = time.time() - start
    print(f"Sort completed in {elapsed:.6f} seconds")
    return sorted_students