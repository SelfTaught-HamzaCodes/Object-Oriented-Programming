import os
import time

from RMS.Managing import Management
from RMS.KeyValidation import KeyValidation
from RMS.UserAuthentication import UserAuthentication
from RMS.select_seat_UI import SeatsUI
from RMS.Payment_UI import PaymentUI


class Guest(Management):

    @staticmethod
    def cli_helper(user=False):

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            time.sleep(1)
            if user:
                print(F"\t Signed In, {user}. \n")
            else:
                print("\t Signed In, Guest. \n")
            time.sleep(0.2)
            print("\t Press -1- to Reserve a ticket.")
            time.sleep(0.2)
            print("\t Press -2- to View a reserved ticket.")
            time.sleep(0.2)
            print("\t Press -3- to Delete a reserved ticket.")
            time.sleep(0.2)
            print("\t Press -4- to Edit a reserved ticket.")
            time.sleep(0.2)
            print("\t Press -5- to Return to previous menu.")
            time.sleep(0.2)
            print("\t Press -6- to Exit Program.")

            user_cli = input("\t Choose: ")

            if user_cli == "1":
                Guest.reserve_ticket(user)
                input("\t Press Enter to proceed: ")
                continue

            if user_cli == "2":
                Guest.view_tickets(user)
                input("\t Press Enter to proceed: ")
                continue

            if user_cli == "3":
                Guest.delete_ticket()
                input("\t Press Enter to proceed: ")
                continue

            if user_cli == "4":
                Guest.edit_ticket()
                input("\t Press Enter to proceed: ")
                continue

            if user_cli == "5":
                break

            if user_cli == "6":
                quit()

    @classmethod
    def check_ticket_id(cls):
        """
        A helper function to get dictionary at key: ticket id.
        from: Managing.Management.tickets

        :return:
        ticket_id_dict, dict, a dictionary containing values for the ticket id.
        ticket_id, str, the ticket id.

        False, bool, this shows that the ticket_id entered couldn't be located.
        ticket_id, str, the ticket id.
        """

        while True:
            ticket_id = input("\t Ticket ID: ")

            ticket_id_dict = Management.tickets.get(ticket_id, 0)

            if ticket_id_dict:
                return ticket_id_dict, ticket_id

            else:
                print(f"\t Ticket ID: {ticket_id} not found.")
                return False, ticket_id

    @classmethod
    def reserve_ticket(cls, user=False):

        Management.ticket_id += 1

        # Call the increment reference that takes an int and converts it into a reference number:str.
        # Management.ticked_id = 2 --> "PRW-00002"
        ticket_id = Management.increment_reference(t_id=Management.ticket_id)

        # Create a dictionary with the new key, PRW-00002
        Management.tickets[ticket_id] = {}

        # Enter Personal Details:
        # Keys = First Name, Last Name, Age, Identity Number, Contact Number, Departure City, Arrival City.
        for key in Management.tickets["DONT DELETE"].keys():

            # Pass Key and the KeyValidation's helper method will pass the key to the respective function to handle.
            # KeyValidation -> helper (returns: key value or False) -> respective Function (returns: value or False)
            key_value = KeyValidation.helper(key)

            if key_value:
                Management.tickets[ticket_id][key] = key_value

            # If 'quit' typed in helper quit by deleting the incomplete dictionary.
            else:
                del Management.tickets[ticket_id]
                Management.ticket_id -= 1
                break

        # Display Available Trains:
        # Using ticket id, we find the arrival and departure by find_train in Management.
        returned, availability = Management.find_train(ticket_id)

        if not returned:
            print(availability)
            del Management.tickets[ticket_id]
            Management.ticket_id -= 1

        else:

            print("\n\t Available Trains: \n")

            # availability will be a list of train id's.
            for train in availability:
                print(F'\t ID:{train} - Name: {Management.trains[train]["Train Name"]} \n'
                      F'\t {Management.trains[train]["Available Classes"]}')

            selected_id = ""
            while selected_id != "quit":

                selected_id = input("\t (Type 'quit' to go back) Select a Train ID:  ")

                # If the selected ID is in the list above:
                if selected_id in availability:
                    select_class = input("\t (Type 'quit' to go back) Select your class: ")

                    # SeatsUI.seats = dict -> train_id -> class
                    selected_class = SeatsUI.seats[selected_id].get(select_class, 0)

                    if selected_class:
                        select_seats = input("\t (Type 'quit' to go back) Number of seats: ")

                        # class = dict -> seats -> available_seats
                        seats_available = selected_class["Seats"]

                        # check if seats available:
                        if int(seats_available) >= int(select_seats):
                            status, seats = SeatsUI.book_seats(selected_id, select_class, int(select_seats))

                            if not status:
                                selected_id = "quit"
                                break

                            # payment time
                            else:
                                status, cost = PaymentUI.cli_helper(selected_id, select_class, select_seats)

                                if user:
                                    # in the user's list have a list of all ticket id booked in a list.
                                    UserAuthentication.get_user(user)["Tickets"].append(ticket_id)

                                if status:
                                    # append list key = {}, heading = values
                                    headings = ["Train ID", "Class", "Seats", "Seat Numbers", "Payment"]
                                    values = [selected_id, select_class, select_seats, seats, cost]

                                    Management.tickets[ticket_id]["Booking"] = {}

                                    for heading, value in zip(headings, values):
                                        Management.tickets[ticket_id]["Booking"][heading] = value

                                    print(F"\t Your account been deducted by PKR{cost}")
                                    print(F"\n \t Ticket Generated! Your ID is: {ticket_id}")

                                    break

                                else:
                                    selected_id = "quit"
                                    break

                        elif selected_class == "quit":
                            selected_id = "quit"
                            break

                        else:
                            print("\t Sorry, we are short on remaining seats.")

                    elif select_class == "quit":
                        selected_id = "quit"
                        break

                    else:
                        print(F"\t {select_class} doesn't exist")

                else:
                    print("\t Invalid ID")

            if selected_id == "quit":
                del Management.tickets[ticket_id]
                Management.ticket_id -= 1

    @classmethod
    def view_tickets(cls, user=False):

        if user:
            tickets_booked = UserAuthentication.get_user(user)["Tickets"]

            if tickets_booked:

                print(f"\t ID: {user}'s tickets (New to Old).")

                for ticket in reversed(tickets_booked):
                    print("\t" + F"ID: {ticket} --> " + str(Management.tickets.get(ticket)))
            else:
                print(f"\t No tickets booked by {user}.")

        else:
            t_id_dict, t_id = Guest.check_ticket_id()

            if t_id_dict:

                print(f"\n\t Ticket ID: {t_id}")

                for key, value in t_id_dict.items():
                    print("\t", key, ":", value)

            else:
                return False

    @classmethod
    def delete_ticket(cls):

        t_id_dict, t_id = Guest.check_ticket_id()

        if t_id_dict:

            print(f"\t Please confirm would you like to delete {t_id}.")
            confirmation = input("\t Press -1- for Yes | Press -2- for No ")

            if confirmation == "1":
                del Management.tickets[t_id]
                print(f"\t ID: {t_id} was deleted.")

            else:
                return False

        else:
            return False

    @classmethod
    def edit_ticket(cls):

        t_id_dict, t_id = Guest.check_ticket_id()

        if t_id_dict:

            print("\t" + str(t_id_dict))
            change = ""

            while change != "quit":
                change = input("\t (Type 'quit' to go back) Enter a key you would like to change: ")

                if t_id_dict.get(change, 0):
                    value_change = KeyValidation.helper(change)

                    if value_change:
                        t_id_dict[change] = value_change
                        print(f"\t Key: {change}'s value changed to: {value_change}")

                else:
                    print("\t Enter a valid key.")
                    continue
