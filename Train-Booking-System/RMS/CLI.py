# This will be the command-line interface (UI) for our Railway Booking System:

# Built-In Imports:
import time
import os

# Self-created Module Imports:
from RMS.UserAuthentication import UserAuthentication
from RMS.Admin_UI import Admin
from RMS.Guest_UI import Guest
from RMS.User_UI import User


def cli():
    while True:

        # Greetings:
        time.sleep(1)
        print("\t WELCOME TO RAILWAY BOOKING SYSTEM \n")
        time.sleep(1)
        print("\t \t Project Prepared by:")
        time.sleep(1)
        print("\t \t --------------------")
        time.sleep(1)
        print("\t \t Muhammad Hamza Saeed")

        time.sleep(3)

        # This statement is used to clear the terminal:
        os.system('cls' if os.name == 'nt' else 'clear')

        # User Authentication:
        # 3 options will be displayed: 1st for Guest, 2nd for User, 3rd for Admin.

        user_options = [str(i) for i in range(1, 4)]

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            time.sleep(0.1)
            print("\t Choose an option:")
            time.sleep(0.1)
            print("\t 1 for Guest.")
            time.sleep(0.1)
            print("\t 2 for User.")
            time.sleep(0.1)
            print("\t 3 for Admin.")

            user_option = input("\t Choose: ")

            if user_option not in user_options:
                print("Choose a valid option.")
                continue

            else:

                os.system('cls' if os.name == 'nt' else 'clear')

                # Initialized User Authentication to be later called be by Admin / User to validate credentials.
                UAS = UserAuthentication()

                # If "GUEST" is selected.
                if user_option == "1":
                    Guest.cli_helper()

                # If "USER" is selected.
                elif user_option == "2":

                    sign_in_up = ""

                    while sign_in_up not in ["1", "2"]:

                        sign_in_up = input("\t Press '1' to Sign Up | Press '2' to Sign In | Press 'Q' to Go back: ")

                        if sign_in_up == "1":

                            # if "SIGN-UP" is selected, we go to CLI --> USER_AUTHENTICATION.
                            authentication = UAS.sign_up()

                            # if "SIGN-UP" was successful, we pass the USERNAME as an argument to USER_UI.
                            if authentication:
                                User.cli_helper(authentication)

                        elif sign_in_up == "2":

                            # if "SIGN-IN" is selected, we go to CLI --> USER_AUTHENTICATION.
                            authentication = UAS.sign_in()

                            # if "SIGN-IN" was successful, we pass the USERNAME as an argument to USER_UI.
                            if authentication:
                                User.cli_helper(authentication)

                        else:
                            print("Choose a valid option.")
                            break

                # If "ADMIN" is selected.
                elif user_option == "3":

                    # if "ADMIN" was selected, CLI --> USER_AUTHENTICATION.
                    if UAS.sign_in():

                        # if "SIGN-IN" was successful, CLI --> ADMIN_UI
                        Admin.cli_helper()






