class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grade = grade


students = []


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
    pass


def update_grade():
    pass


def delete_student():
    pass


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