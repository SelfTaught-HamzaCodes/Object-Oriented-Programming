from student_management_system import StudentManagementSystem
import time


def main():
    # Timeout (in seconds)
    x = 3

    while True:
        user_choice = input("""\n-Student Management System-

1- ADD A STUDENT.
2- SEARCH A STUDENT.
3- DELETE A STUDENT.
4- DISPLAY ALL STUDENTS.
5 - QUIT.

Select: """)

        try:
            if int(user_choice) not in range(1, 7):
                print("Choose a valid option\n")
                continue

        except ValueError:
            print("Choose a valid option\n")
            continue

        if user_choice == "1":
            name = input("Student's Name: ")
            marks_1 = int(input("Student's Age: "))
            marks_2 = int(input("Student's Grade: "))

            StudentManagementSystem(name, marks_1, marks_2)
            time.sleep(x)

        elif user_choice == "2" or user_choice == "3":
            roll_number = int(input("Enter a Roll Number: "))

            if user_choice == "2":
                print(StudentManagementSystem.search_student(roll_number))
                time.sleep(x)

            else:
                print(StudentManagementSystem.delete_student(roll_number))
                time.sleep(x)

        elif user_choice == "4":
            StudentManagementSystem.display_all_students()
            time.sleep(x)

        else:
            quit()


main()
