class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.marks = {}

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        num_students = int(input("Enter the number of students: "))
        return num_students

    def input_student_information(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self.students.append(Student(student_id, name, dob))

    def input_number_of_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        return num_courses

    def input_course_information(self):
        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks_for_course(self):
        course_id = input("Enter the course ID to input marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("Course not found!")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
            course.marks[student.student_id] = mark

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("Course not found!")
            return

        print(f"Marks for course {course.name}:")
        for student_id, mark in course.marks.items():
            student = next((s for s in self.students if s.student_id == student_id), None)
            if student:
                print(f"Student: {student.name} (ID: {student_id}), Mark: {mark}")

if __name__ == "__main__":
    smm = StudentMarkManagement()

    while True:
        print("\n1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            smm.input_student_information()
        elif choice == "2":
            smm.input_course_information()
        elif choice == "3":
            smm.input_marks_for_course()
        elif choice == "4":
            smm.list_courses()
        elif choice == "5":
            smm.list_students()
        elif choice == "6":
            smm.show_student_marks()
        elif choice == "0":
            break
        else:
            print("Invalid choice! Please try again.")
