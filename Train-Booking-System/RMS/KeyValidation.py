# A class for making key validations for our two dictionaries (TICKETS, TRAINS, USERS):

import re


class KeyValidation:

    @classmethod
    def helper(cls, key):

        key_value = ""

        while True:

            if key not in ["Departure City", "Arrival City", "Train Source", "Train Destination", "Available Classes", "Card Credentials"]:
                key_value = input(F"\t (Type 'quit' to go back) {key}: ")

                if key_value == "quit":
                    return False

            if key in ["First Name", "Last Name", "Train Name"]:

                if cls.string_validation(key_value):
                    return key_value
                else:
                    continue

            elif key in ["Identity Number", "Contact Number", "Train Departure", "Train Arrival", "Card Credentials"]:

                if cls.re_validation(key, key_value):
                    if key != "Card Credentials":
                        return key_value
                    else:
                        return True
                else:
                    continue

            elif key in ["Age", "Seats Available", "Seats", "Payment"]:

                if cls.int_validation(key_value):
                    return int(key_value)
                else:
                    continue

            elif key in ["Departure City", "Arrival City", "Train Source", "Train Destination", "Available Classes"]:

                result = cls.option_validation(key, key_value)

                if result:
                    return result
                else:
                    continue

    @classmethod
    def string_validation(cls, string_value):

        if len(string_value) > 256:
            print("\t Enter a valid string, max length: 255")
            return False

        else:
            return string_value

    @classmethod
    def re_validation(cls, re_key, re_value):

        if re_key == "Identity Number":
            matched = re.compile(r"^\d{5}-\d{7}-\d$").match(re_value)

            if matched:
                return re_value

            else:
                print("\t Enter a Valid Identification Number (Format: XXXXX-XXXXXXX-X)")
                return False

        if re_key == "Contact Number":
            matched = re.compile(r"^03\d{2}-\d{7}$").match(re_value)

            if matched:
                return re_value
            else:
                print("\t Enter a Valid Contact Number (Format: 03XX-XXXXXXX")
                return False

        if re_key == "Train Departure" or re_key == "Train Arrival":
            matched = re.compile(r"^\d{2}:\d{2}$").match(re_value)

            if matched:
                return re_value

            else:
                print("\t Enter a Valid Time (Format: XX:XX)")
                return False

        if re_key == "Card Credentials":

            visa = re.compile(r"^4\d{15}$")
            mc = re.compile(r"^5[1-5]\d{14}$")
            expiry_date = re.compile(r"^(0[1-9]|1[0-2])-(\d{2})$")

            card_number = input("\t Enter your card: ")
            csv = input("\t Enter your CSV: ")
            expiry = input("\t Enter Expiry (Fornat: MM-YY): ")

            if visa.match(card_number) or mc.match(card_number):
                if len(csv) == 3:
                    if expiry_date.match(expiry):
                        return True

                    else:
                        print("\t Enter a valid Expiry Date.")
                        return False
                else:
                    print("\t Enter a valid CSV number.")
                    return False
            else:
                print("\t Enter a valid card number.")
                return False

    @classmethod
    def int_validation(cls, int_value):

        try:
            if int(int_value) < 0:
                print("\t Enter a positive integer less than 100.")
                return False

            else:
                return int_value

        except ValueError:
            print("\t Enter a positive integer less than 100.")
            return False

    @classmethod
    def option_validation(cls, option_key, option_value):

        cities = {
            "KHI": "Karachi",
            "LHR": "Lahore",
            "ISL": "Islamabad",
            "UET": "Quetta",
            "PEW": "Peshawar"
        }

        classes = {
            "EC": "Economy",
            "AL": "AC Lower",
            "AB": "AC Business"
        }

        if option_key == "Available Classes":
            for key, value in classes.items():
                print("\t " + key + ":" + value)

            class_train = input("\t Enter Key (Format: EC-AL-AB): ")
            class_price = input(f"\t Enter Price for {class_train} (Format: PRICE-PRICE-PRICE): ")
            class_seat = input(f"\t Enter Seats for {class_train} (Format: SEAT-SEAT-SEAT): ")

            valid_selections = {}

            for selection, price, seat in zip(class_train.split("-"), class_price.split("-"), class_seat.split("-")):
                if not classes.get(selection, 0):
                    print(f"\t Invalid Key {selection} entered")
                    break

                else:
                    valid_selections[classes.get(selection)] = {"Price": price, "Seats": seat}
            else:
                return valid_selections

        else:
            for key, value in cities.items():
                print("\t " + key + ":" + value)

            destination = input(f"\t Enter Key for {option_key}: ")

            if cities.get(destination, 0):
                return cities.get(destination)
            else:
                print("\t Enter a valid destination key.")
                return False
