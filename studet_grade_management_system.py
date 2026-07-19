import json
import os


class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grade = grade


students = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to return to menu...")


def export_data():
    export_file = os.path.join(os.path.dirname(__file__), "students_export.json")
    data = [
        {
            "student_id": student.student_id,
            "name": student.name,
            "course": student.course,
            "grade": student.grade,
        }
        for student in students
    ]
    with open(export_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print(f"Data exported to {export_file}.")


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    grade = input("Enter grade: ")

    student = Student(student_id, name, course, grade)
    students.append(student)
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
            print("Grade updated successfully.")
            return
    print("Student not found.")


def delete_student():
    delete_id = input("Enter student ID to delete: ")
    for student in students:
        if student.student_id == delete_id:
            students.remove(student)
            print("Student deleted successfully.")
            return
    print("Student not found.")


def show_statistics():
    if not students:
        print("No students found.")
        return

    valid_students = []
    for student in students:
        try:
            grade_value = float(student.grade)
            valid_students.append((student, grade_value))
        except ValueError:
            continue

    if not valid_students:
        print("No valid numeric grades available.")
        return

    count = len(valid_students)
    total = sum(grade for _, grade in valid_students)
    average = total / count

    highest_student, highest_grade = max(valid_students, key=lambda item: item[1])
    lowest_student, lowest_grade = min(valid_students, key=lambda item: item[1])

    passing_threshold = 60.0
    passed = sum(1 for _, grade in valid_students if grade >= passing_threshold)
    failed = count - passed
    pass_rate = (passed / count) * 100
    fail_rate = (failed / count) * 100

    print(f"Number of students: {count}")
    print(f"Average grade: {average:.2f}")
    print(f"Highest grade student: {highest_student.name} (ID: {highest_student.student_id}) - Grade: {highest_grade}")
    print(f"Lowest grade student: {lowest_student.name} (ID: {lowest_student.student_id}) - Grade: {lowest_grade}")
    print(f"Pass rate: {pass_rate:.2f}%")
    print(f"Fail rate: {fail_rate:.2f}%")


def sort_students():
    pass


def main():
    while True:
        clear_screen()
        print("==================================")
        print("Student Grade Management System")
        print("==================================")
        print()
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Update Grade")
        print("5 Delete Student")
        print("6 Statistics")
        print("7 Export Data")
        print("8 Exit")
        print()

        choice = input("Select option: ")

        if choice == "1":
            add_student()
            pause()

        elif choice == "2":
            view_students()
            pause()

        elif choice == "3":
            search_student()
            pause()

        elif choice == "4":
            update_grade()
            pause()

        elif choice == "5":
            delete_student()
            pause()

        elif choice == "6":
            show_statistics()
            pause()

        elif choice == "7":
            export_data()
            pause()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            pause()


if __name__ == "__main__":
    main()