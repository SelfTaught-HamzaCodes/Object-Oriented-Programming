# Student Management System:

class StudentManagementSystem:
    # Class Attributes:
    roll_numbers = 0000
    students = {}

    # Instance Attribute:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

        # Incrementing roll number:
        StudentManagementSystem.roll_numbers += 1

        # Assigns the object an attribute roll_number:
        self.roll_number = StudentManagementSystem.roll_numbers

        # Set roll number as the key, and the object as the value:
        StudentManagementSystem.students[self.roll_number] = self

    # To represent objects in the list in a representable way:
    def __repr__(self):
        return F"StudentManagementSystem({self.name}, {self.age}, {self.grade})"

    # To list all student:
    @classmethod
    def display_all_students(cls):
        """
        Display all students in the system, along with their details.
        """

        print("-Students-")
        for roll_number, details in cls.students.items():
            print(F"{roll_number}. {details.name} | Age: {details.age} | Grade: {details.grade}")

    # To search for a student:
    @classmethod
    def search_student(cls, roll_number):
        """
        Search for a student using their roll number.
        :param roll_number: roll number for a student.
        :return: displays the details for a student if found, else an error message is shown.
        """

        if cls.students.get(roll_number, 0):
            return F"""-Student Found-
Name    : {cls.students[roll_number].name}
RollNo  : {roll_number}
Age     : {cls.students[roll_number].age}
Grade   : {cls.students[roll_number].grade}"""

        else:
            return F"Roll Number: {roll_number} not found!"

    # To delete a student:
    @classmethod
    def delete_student(cls, roll_number):
        """
        Delete a student.
        :param roll_number: roll number for a student.
        :return: display a success message if the removal was successful, else an error message is shown.
        """
        if cls.students.get(roll_number, 0):
            cls.students.pop(roll_number)
            return F"{cls.students[roll_number].name} (Roll Number: {roll_number}) deleted!"
        else:
            return F"Roll Number: {roll_number} not found!"
