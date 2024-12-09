class Students:
    __students = []

    def input(self):
        n = int(input("Enter the number of students: "))
        for _ in range(n):
            student_id = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Date of Birth (dd/mm/yyyy): ")
            self.__students.append({"id": student_id, "name": name, "dob": dob})

    def list(self):
        if len(self.__students) == 0:
            print("There are no students\n")
            return
        print("\nList of Students:")
        for student in self.__students:
            print(f"- {student['id']}: {student['name']}, DoB: {student['dob']}")

    def get_students(self):
        return self.__students


class Courses:
    __courses = []

    def input(self):
        n = int(input("Enter the number of courses: "))
        for _ in range(n):
            course_id = input("Course ID: ")
            name = input("Course Name: ")
            self.__courses.append({"id": course_id, "name": name})

    def list(self):
        if len(self.__courses) == 0:
            print("There are no courses\n")
            return
        print("\nList of Courses:")
        for course in self.__courses:
            print(f"- {course['id']}: {course['name']}")

    def get_courses(self):
        return self.__courses


class Marks:
    __marks = {}
    __courses = []
    __students = []

    def __init__(self, courses, students):
        self.__courses = courses
        self.__students = students

    def input(self):
        for course in self.__courses:
            course_id = course["id"]
            print(f"Entering marks for course: {course['name']} (ID: {course_id})")
            course_marks = {}
            for student in self.__students:
                mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
                course_marks[student["id"]] = mark
            self.__marks[course_id] = course_marks

    def list(self):
        course_id = input("Enter course ID: ")
        course = next((c for c in self.__courses if c["id"] == course_id), None)
        if course is None:
            print("Course not found!")
            return
        print(f"\nMarks for course: {course['name']} (ID: {course_id})")
        for student in self.__students:
            student_id = student["id"]
            mark = self.__marks.get(course_id, {}).get(student_id, None)
            if mark is not None:
                print(f"{student['name']} (ID: {student_id}): {mark}")
            else:
                print(f"{student['name']} (ID: {student_id}): No mark available")


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def input_functions():
    print("Input Functions:\n"
          "1. Input students\n"
          "2. Input courses\n"
          "3. Input marks\n"
          "4. Back")
    option1 = int(input("Select: "))
    if option1 < 1 or option1 > 4:
        input_functions()
    elif option1 == 4:
        return
    else: selector[option1 - 1].input()

def list_functions():
    print("Input Functions:\n"
          "1. List students\n"
          "2. List courses\n"
          "3. List marks\n"
          "4. Back")
    option1 = int(input("Select: "))
    if option1 < 1 or option1 > 4:
        list_functions()
    elif option1 == 4:
        return
    else: selector[option1 - 1].list()

def prompt():
    print(strike("-----------------------------"))
    print("Student management menu: \n"
          "1. Input Functions\n"
          "2. Listing Functions\n"
          "3. Quit")
    option = input("Select: ")
    print(strike("-----------------------------"))
    if option == "1": input_functions()
    if option == "2": list_functions()
    if option == "3": return
    prompt()

students = Students()
courses = Courses()
marks = Marks(courses.get_courses(), students.get_students())
selector = [students, courses, marks]
prompt()
