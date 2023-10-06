# Car Parking System

import sqlite3
from datetime import datetime


class CarParkingSystem:
    """
    A Car Parking System class that implements a program to enter and exit vehicles from a parking lot,
    charging them according to their stay, rates can be manually set.
    All data is stored in a local database, allowing program to retain data.
    """

    # Constants:
    BASE_FARE = 1
    INCREMENT_FARE = 0.50

    # In Hours:
    FREE_TIME = 3
    INCREMENT_TIME = 1

    CURRENCY = "$"
    DATABASE = "cars.db"

    # Initialize a car being parked:
    def __init__(self, number_plate):

        # Connect to the database:
        connect, cursor = CarParkingSystem.__initialize_database()

        # Obtain number plate, if it exists.
        cursor.execute(
            F"SELECT Parked FROM cars_parked WHERE Number_Plate = '{number_plate}' ORDER BY Time_In DESC LIMIT 1")
        parked = cursor.fetchone()
        parked = parked[0] if parked else parked

        # If number plate doesn't exist or the car was previously parked:
        if (not parked) or (parked == "False"):

            check_in = datetime.now()
            time_in = check_in.strftime('%b-%d %H:%M:%S')

            cursor.execute(F'''INSERT INTO cars_parked ('Number_Plate', 'Time_In', 'Parked')
                            VALUES ('{number_plate}', '{time_in}', '{True}' )''')

            print(F"{number_plate} successfully added!")

        else:
            print(F"Car ({number_plate}) is already parked!")

        # Close database connection:
        connect.commit()
        connect.close()

    @classmethod
    def leave_car(cls, number_plate):
        """
        A function to remove car from the database, calculating the charges and displaying the bill.
        """

        # Calculate charges for this number plate:
        information = cls.__calculate_charges(number_plate)

        # Connect to the database:
        connect, cursor = CarParkingSystem.__initialize_database()
        cursor.execute(
            F"SELECT Parked FROM cars_parked WHERE Number_Plate = '{number_plate}' ORDER BY Time_In DESC LIMIT 1")

        parked = cursor.fetchone()
        parked = parked[0] if parked else parked

        # If car is not parked.
        if parked == "False" or not information:
            print(F"{number_plate} not found or not parked.")

        # If car is parked:
        else:

            # Update Information:
            difference, time_out, total_amount = information
            member, parked = False, False

            cursor.execute(F"""UPDATE cars_parked 
                            SET Time_Out = '{time_out}',
                                 Difference = '{difference}',
                                 Amount = '{total_amount}',
                                 Member = '{member}',
                                 Parked = '{parked}'
                             WHERE Number_Plate = '{number_plate}' AND Parked = '{True}'; """)

            # Close Database:
            connect.commit()
            connect.close()

    @classmethod
    def __generate_bill(cls, number_plate, difference, total_amount, extra_time=0):
        """
        A function to generate and display bills in the terminal.
        """

        print(F'''
Number Plate: {number_plate}

Time Elapsed: {difference}

Total Charges: {cls.CURRENCY} {total_amount}

    +++Breakdown+++
    Free Hours: {cls.FREE_TIME} Hour.
    Base Charge: {cls.BASE_FARE}

    Extra Charges: {cls.CURRENCY} {cls.INCREMENT_FARE} every {cls.INCREMENT_TIME} Hours.

    Extra Time: {extra_time}
    *
    {cls.CURRENCY} {cls.INCREMENT_FARE}
    =
    {cls.CURRENCY} {extra_time * cls.INCREMENT_FARE}
    +++''')

    @classmethod
    def __calculate_charges(cls, number_plate):
        """
        Calculate charges for the car with the number plate specified.
        """

        # Connect to database:
        connect, cursor = CarParkingSystem.__initialize_database()

        cursor.execute(
            F"SELECT Time_In FROM cars_parked WHERE Number_Plate = '{number_plate}' AND Parked = 'True' ORDER BY Time_In DESC LIMIT 1")

        result = cursor.fetchone()
        result = result[0] if result else result

        # If car doesn't exist or isn't currently parked:
        if result is None:
            return None

        # Calculate charges:
        else:
            check_out = datetime.now()
            time_out = check_out.strftime('%b-%d %H:%M:%S')

            difference = datetime.strptime(time_out, '%b-%d %H:%M:%S') \
                         - datetime.strptime(result, '%b-%d %H:%M:%S')

            hours = (difference.days * 24) + (difference.seconds // 3600)

            total_amount = 0

            if hours > cls.FREE_TIME:

                extra_time = (hours - cls.FREE_TIME) // cls.INCREMENT_TIME
                extra_charges = cls.INCREMENT_FARE * extra_time

                total_amount += (extra_charges + cls.BASE_FARE)

            else:
                total_amount = cls.BASE_FARE
                extra_time = 0

            # Generate Bill:
            cls.__generate_bill(number_plate, difference, total_amount, extra_time)

            return difference, time_out, total_amount

    @classmethod
    def __initialize_database(cls):

        connect = sqlite3.connect(cls.DATABASE)
        cursor = connect.cursor()

        return connect, cursor
