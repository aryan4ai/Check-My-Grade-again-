import unittest
import csv
import os
from student import Student
from course import Course
from professor import Professor
from utils import search_student, sort_students
import time

TEST_FILE = "data/students.csv"

class TestStudent(unittest.TestCase):

    def setUp(self):
        # Seed 1000 student records
        with open(TEST_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["email_address","first_name","last_name","course_id","grade","marks"])
            writer.writeheader()
            for i in range(1000):
                writer.writerow({
                    "email_address": f"student{i}@mycsu.edu",
                    "first_name": f"First{i}",
                    "last_name": f"Last{i}",
                    "course_id": "DATA200",
                    "grade": "A",
                    "marks": str(60 + (i % 40))
                })

    def test_add_student(self):
        s = Student("new@mycsu.edu", "New", "User", "DATA200", "B", "85")
        s.add_new_student()
        result = search_student("new@mycsu.edu")
        self.assertTrue(len(result) > 0)

    def test_delete_student(self):
        s = Student("", "", "", "", "", "")
        s.delete_student("student0@mycsu.edu")
        result = search_student("student0@mycsu.edu")
        self.assertEqual(len(result), 0)

    def test_update_student(self):
        s = Student("", "", "", "", "", "")
        s.update_student_record("student1@mycsu.edu", "grade", "C")
        result = search_student("student1@mycsu.edu")
        self.assertEqual(result[0]["grade"], "C")

    def test_search_timing(self):
        start = time.time()
        search_student("student999@mycsu.edu")
        elapsed = time.time() - start
        print(f"\nSearch time: {elapsed:.6f}s")
        self.assertLess(elapsed, 1.0)

    def test_sort_by_marks_asc(self):
        results = sort_students(key="marks", reverse=False)
        marks = [float(r["marks"]) for r in results]
        self.assertEqual(marks, sorted(marks))

    def test_sort_by_marks_desc(self):
        results = sort_students(key="marks", reverse=True)
        marks = [float(r["marks"]) for r in results]
        self.assertEqual(marks, sorted(marks, reverse=True))

    def test_sort_by_email(self):
        results = sort_students(key="email_address")
        emails = [r["email_address"] for r in results]
        self.assertEqual(emails, sorted(emails))


class TestCourse(unittest.TestCase):

    def test_add_course(self):
        c = Course("TEST101", "Test Course", "A test")
        c.add_new_course()

    def test_delete_course(self):
        c = Course("", "", "")
        c.delete_new_course("TEST101")


class TestProfessor(unittest.TestCase):

    def test_add_professor(self):
        p = Professor("test@mycsu.edu", "Test Prof", "Lecturer", "DATA200")
        p.add_new_professor()

    def test_delete_professor(self):
        p = Professor("", "", "", "")
        p.delete_professor("test@mycsu.edu")


if __name__ == "__main__":
    unittest.main()