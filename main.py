from student import Student
from course import Course
from professor import Professor
from grades import Grades
from login import LoginUser
from utils import search_student, sort_students

def main_menu():
    print("\n=== CheckMyGrade ===")
    print("1. Student Records")
    print("2. Course Records")
    print("3. Professor Records")
    print("4. Grade Report")
    print("5. Search Student")
    print("6. Sort Students")
    print("7. Login / Password")
    print("0. Exit")
    return input("Choice: ")

def run():
    while True:
        choice = main_menu()
        if choice == "1":
            # Student submenu
            email = input("Email: ")
            fn = input("First Name: ")
            ln = input("Last Name: ")
            cid = input("Course ID: ")
            grade = input("Grade: ")
            marks = input("Marks: ")
            s = Student(email, fn, ln, cid, grade, marks)
            s.add_new_student()
        elif choice == "5":
            email = input("Search email: ")
            result = search_student(email)
            print(result)
        elif choice == "6":
            key = input("Sort by (marks/email_address): ")
            order = input("Descending? (y/n): ").lower() == "y"
            results = sort_students(key=key, reverse=order)
            for r in results[:10]:
                print(r)
        elif choice == "0":
            print("Goodbye.")
            break

if __name__ == "__main__":
    run()