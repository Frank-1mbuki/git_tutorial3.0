import json
import os


class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grade = grade


STUDENTS_FILE = os.path.join(os.path.dirname(__file__), "students.json")


def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []

    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

    students = []
    for item in data:
        student_id = item.get("student_id")
        name = item.get("name")
        course = item.get("course")
        grade = item.get("grade")
        if student_id is not None:
            students.append(Student(student_id, name, course, grade))
    return students


def save_students():
    data = [
        {
            "student_id": student.student_id,
            "name": student.name,
            "course": student.course,
            "grade": student.grade,
        }
        for student in students
    ]

    with open(STUDENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


students = load_students()


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    grade = input("Enter grade: ")

    student = Student(student_id, name, course, grade)
    students.append(student)
    save_students()
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    for student in students:
        print(f"ID: {student.student_id}, Name: {student.name}, Course: {student.course}, Grade: {student.grade}")


def search_student():
    search_id = input("Enter student ID to search: ")
    for student in students:
        if student.student_id == search_id:
            print(f"ID: {student.student_id}, Name: {student.name}, Course: {student.course}, Grade: {student.grade}")
            return
    print("Student not found.")


def update_grade():
    search_id = input("Enter student ID to update grade: ")
    for student in students:
        if student.student_id == search_id:
            new_grade = input("Enter new grade: ")
            student.grade = new_grade
            save_students()
            print("Grade updated successfully.")
            return
    print("Student not found.")


def delete_student():
    delete_id = input("Enter student ID to delete: ")
    for student in students:
        if student.student_id == delete_id:
            students.remove(student)
            save_students()
            print("Student deleted successfully.")
            return
    print("Student not found.")


def show_statistics():
    pass


def sort_students():
    pass


def main():
    while True:
        print("\n===== Student Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Grade")
        print("5. Delete Student")
        print("6. Statistics")
        print("7. Sort Students")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_grade()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_statistics()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()