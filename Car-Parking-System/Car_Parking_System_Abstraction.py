import Car_Parking_System
import time
import subprocess


def main():
    """
    Acts as an abstraction for Car Parking System.
    """

    while True:
        option = input("""
Welcome to Car Parking System:

1- Enter a Car (Check-in).
2- Remove a Car (Check-out). 
3- Quit

Choose an option: """)

        if option not in ["1", "2", "3"]:
            print("Error: Choose a valid option to proceed.")
            continue

        else:
            if option == "1":
                number_plate = input("Number Plate: ")
                Car_Parking_System.CarParkingSystem(number_plate)
                time.sleep(3)

                # Windows
                subprocess.call('cls', shell=True)
                continue

            elif option == "2":
                number_plate = input("Number Plate: ")
                Car_Parking_System.CarParkingSystem.leave_car(number_plate)
                time.sleep(3)

                # Windows
                subprocess.call('cls', shell=True)
                continue

            else:
                quit()


main()
