from typing import List


class Student:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height


def average_heights():
    students_container: List[Student] = []
    while True:
        try:
            decisition = input(
                "Do you want to add a new Student or find the the studen with the average height. Type Add or Average or Total: \n "
            ).lower()
            if decisition == "add":
                while True:
                    student_name = input(
                        "Please introduce the name of the student or N for end to update students: \n"
                    )
                    if student_name == "n" or student_name == "N":
                        print("Leaving Add student section.")
                        break
                    student_height = float(
                        input("Please, enter your students heights: \n")
                    )
                    if student_height > 2.5:
                        print("Introduce realistic height")
                    else:
                        student = Student(student_name, student_height)
                        students_container.append(student)
                        print("Student added successfully")
            elif decisition == "average":
                average_height = 0
                actual_student = 0
                for student in students_container:
                    if student.height > average_height:
                        average_height = student.height
                        actual_student = student.name
                print(average_height, actual_student, "mts")
            elif decisition == "total":
                for student in students_container:
                    print(student.name)

        except ValueError:
            print("Please enter valid data")


average_heights()
