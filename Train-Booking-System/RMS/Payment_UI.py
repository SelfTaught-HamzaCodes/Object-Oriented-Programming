from RMS.Managing import Management
from RMS.KeyValidation import KeyValidation


class PaymentUI:

    @classmethod
    def cli_helper(cls, train_id: str, train_class: str, train_seats: str):
        cost = cls.get_payment(train_id, train_class, train_seats)
        print(F"\t Your ({train_seats}) Seats will cost you: Rs.{cost}")
        print("\t Press -1- to pay via Easy Paisa | Jazz Cash.")
        print("\t Press -2- to pay via Debit Card | Credit Card.")
        print("\t Press -3- to quit.")

        while True:

            payment_choice = input("\t Choose an option: ")

            if payment_choice == "1":
                if KeyValidation.helper("Contact Number"):
                    return "\t Payment was successful", cost

                else:
                    print("\t Enter a valid mobile number.")
                    continue

            elif payment_choice == "2":
                if KeyValidation.helper("Card Credentials"):
                    return "\t Payment was successful.", cost

                else:
                    print("\t Enter valid card credentials")
                    continue

            elif payment_choice == "3":
                return False, False

            else:
                print("\t Choose a valid option.")
                continue

    @classmethod
    def get_payment(cls, train_id: str, train_class: str, train_seats: str):
        seat_price = Management.trains[train_id]["Available Classes"][train_class]["Price"]
        return int(seat_price) * int(train_seats)
