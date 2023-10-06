from RMS.KeyValidation import KeyValidation
from RMS.Managing import Management
from RMS.select_seat_UI import SeatsUI

import time
import os


class Admin(Management):

    @staticmethod
    def cli_helper():

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            time.sleep(1)
            print("\t WELCOME TO THE ADMIN PANEL \n")
            time.sleep(0.2)
            print("\t Press -1- to View all tickets.")
            time.sleep(0.2)
            print("\t Press -2- to Modify a ticket.")
            time.sleep(0.2)
            print("\t Press -3- to View all trains.")
            time.sleep(0.2)
            print("\t Press -4- to View Add/Modify trains")
            time.sleep(0.2)
            print("\t Press -q- to Return to previous menu.")
            time.sleep(0.2)

            admin_cli = input("\t Choose: ")

            if admin_cli == "1":
                Admin.view_all_tickets()
                input("\t Press Enter to proceed: ")
                continue

            elif admin_cli == "2":
                ticket_id = input("\t Enter the ticket id: ")
                Admin.modify_ticket(ticket_id)
                input("\t Press Enter to proceed: ")
                continue

            elif admin_cli == "3":
                Admin.view_all_trains()
                input("\t Press Enter to proceed: ")
                continue

            elif admin_cli == "4":
                train_id = input("\t Enter the train id: ")
                Admin.add_modify_train(train_id)
                input("\t Press Enter to proceed: ")

            elif admin_cli == "q":
                break

            else:
                continue

    @classmethod
    def view_all_tickets(cls):

        # As Admin class inherits from Managing, we can access the methods | attributes of Management using cls.
        for ticket_id, details in cls.tickets.items():
            print("\t Ticket ID: ", ticket_id, details)

    @classmethod
    def modify_ticket(cls, ticket_id):

        # Managing.Management.tickets (dict).get (ticket_id a key)
        if cls.tickets.get(ticket_id, 0):
            print("\t" + str(cls.tickets.get(ticket_id)))

            while True:
                change_detail = input("\t Which detail would you like to change (Enter Key): ")

                if cls.tickets[ticket_id].get(change_detail, 0):
                    key_value = KeyValidation.helper(change_detail)

                    if key_value:
                        cls.tickets[ticket_id][change_detail] = key_value
                        print(F"\t {change_detail} successfully changed to: {key_value}")

                    else:
                        break

                else:
                    print(f"\t {change_detail} not found in {ticket_id}.")
                    break
        else:
            print(f"\t {ticket_id} not found.")

    @classmethod
    def view_all_trains(cls):
        for train_id, details in cls.trains.items():
            print("\t Train ID: ", train_id, details)

    @classmethod
    def add_modify_train(cls, train_id):
        if cls.trains.get(train_id, 0):
            print("\t" + str(cls.trains.get(train_id)))

            while True:
                change_detail = input("\t Which detail would you like to change (Enter Key): ")

                if cls.trains[train_id].get(change_detail, 0):
                    key_value = KeyValidation.helper(change_detail)
                    if key_value:
                        cls.trains[train_id][change_detail] = key_value
                        print(F"\t {change_detail} successfully changed to: {key_value}")

                    else:
                        break

                else:
                    print(f"\t {change_detail} not found in {train_id}.")
                    break

        else:
            print(f"\t {train_id} not found.")

            add_train = input(f"\t Would you like to add this train (with ID: {train_id}) | Y-Yes or N-No: ")
            if add_train == "Y":

                cls.trains[train_id] = {}

                for key in cls.trains["DONT DELETE"].keys():
                    key_value = KeyValidation.helper(key)

                    if key_value:
                        cls.trains[train_id][key] = key_value

                    else:
                        del cls.trains[train_id]
                        break
                else:
                    SeatsUI.set_seats()
