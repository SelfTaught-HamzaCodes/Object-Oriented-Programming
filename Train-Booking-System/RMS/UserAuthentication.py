# User-Authentication:


# Imports:
import re


class UserAuthentication:
    # This will hold all users:
    # key: username, value: password
    __users = {
        "ADMIN1234": {"Password": "ADMIN1234", "Tickets": ["DONT DELETE"]},
    }

    @staticmethod
    def __validate(input_type):
        validate_un_pw = re.compile(r"^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")

        entry = ""

        while entry != "quit":

            entry = input(F"\t (Type 'quit' to go back) {input_type}: ")

            match_entry = validate_un_pw.match(entry)

            if match_entry:
                exist = UserAuthentication.__users.get(entry, 0)

                if not exist or input_type == "Password":
                    return entry

                elif exist:
                    print(F"\t {entry} is already taken!")
                    continue

            else:
                print(F"\t Enter a valid {input_type}!")
                continue

        return False

    @staticmethod
    def sign_up():

        ask_username = UserAuthentication.__validate("Username")
        ask_password = UserAuthentication.__validate("Password")

        if ask_username and ask_password:

            UserAuthentication.__users[ask_username] = {"Password": ask_password, "Tickets": []}
            print(F"\t {ask_username} successfully signed up.")
            return ask_username

        else:
            return False

    @staticmethod
    def sign_in():
        # Keep track of failed attempts (max=3):
        failed_attempts = 0

        while failed_attempts < 3:
            # Ask sign_in credentials from user:
            ask_username = input("\t Username: ")
            ask_password = input("\t Password: ")

            fetch = UserAuthentication.__users.get(ask_username, 0)

            if not fetch or fetch["Password"] != ask_password:
                print("\t Invalid Username or Password")
                failed_attempts += 1

            else:
                print(F"\t Welcome back {ask_username}!")
                return ask_username

        if failed_attempts == 3:
            print("\t Too many failed attempts, account locked!")
            return False

    @staticmethod
    def _show_users():
        for un, pw in UserAuthentication.__users.items():
            print(un, "-", pw)

    @staticmethod
    def get_user(key):
        return UserAuthentication.__users.get(key, 0)


if __name__ == "__main__":
    UserAuthenticationSystem = UserAuthentication()

    while True:
        UserAuthenticationSystem.sign_up()
        UserAuthenticationSystem._show_users()
        UserAuthenticationSystem.sign_up()
