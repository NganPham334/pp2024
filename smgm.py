# TODO: clean up this mess or make it disappear

students = []
courses = []
marks = {}

def input_students():
      n = int(input("Enter the number of students: "))
      for _ in range(n):
            student_id = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Date of Birth (dd/mm/yyyy): ")
            students.append({"id": student_id, "name": name, "dob": dob})

def input_courses():
      n = int(input("Enter the number of courses: "))
      for _ in range(n):
            course_id = input("Course ID: ")
            name = input("Course Name: ")
            courses.append({"id": course_id, "name": name})

def input_marks():
      for course in courses:
            course_id = course["id"]
            print(f"Entering marks for course: {course['name']} (ID: {course_id})")
            course_marks = {}
            for student in students:
                  mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
                  course_marks[student["id"]] = mark
            marks[course_id] = course_marks

def list_courses():
      print("\nList of Courses:")
      for course in courses:
            print(f"- {course['id']}: {course['name']}")

def list_students():
      print("\nList of Students:")
      for student in students:
            print(f"- {student['id']}: {student['name']}, DoB: {student['dob']}")

def show_course_marks():
      course_id = input("Enter course ID: ")
      course = next((c for c in courses if c["id"] == course_id), None)
      if course is None:
            print("Course not found!")
            return
      print(f"\nMarks for course: {course['name']} (ID: {course_id})")
      for student in students:
            student_id = student["id"]
            mark = marks.get(course_id, {}).get(student_id, None)
            if mark is not None:
                  print(f"{student['name']} (ID: {student_id}): {mark}")
            else:
                  print(f"{student['name']} (ID: {student_id}): No mark available")

def input_functions():
      print("Input Functions:\n"
            "1. Input students\n"
            "2. Input courses\n"
            "3. Input marks\n"
            "4. Back")
      option1 = input("Select: ")
      if option1 == "1": input_students()
      if option1 == "2": input_courses()
      if option1 == "3": input_marks()
      if option1 == "4": return
      else: input_functions()


def list_functions():
      print("List Functions:\n"
            "1. List students\n"
            "2. List courses\n"
            "3. List course marks\n"
            "4. Back")
      option2 = input("Select: ")
      if option2 == "1": list_students()
      if option2 == "2": list_courses()
      if option2 == "3": show_course_marks()
      if option2 == "4": return
      else: list_functions()


def main():
      print("Student management menu: \n"
            "1. Input Functions\n"
            "2. Listing Functions\n"
            "3. Quit")

      option = input("Select: ")
      if option == "1": input_functions()
      if option == "2": list_functions()
      if option == "3": return
      else: main()

if __name__ == "__main__":
    main()