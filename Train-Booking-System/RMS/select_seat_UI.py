# Display seats to select:
import re
from RMS.Managing import Management


class SeatsUI:

    bp = F''' \t
         O - Available | X - Not Available
         ==========================
         |O-A1, O-A2, O-A3        |
         |-------------           |
         |O-A4, O-A5, O-A6        |
         |+++++++++++++           |
         |O-B1, O-B2, O-B3        |
         |-------------           |
         |O-B4, O-B5, O-B6        |
         |+++++++++++++           | 
         |O-C1, O-C2, O-C3        |
         |-------------           |
         |O-C4, O-C5, O-C6        |
         |+++++++++++++           |              
         |O-D1, O-D2, O-D3        |
         |-------------           |
         |O-D4, O-D5, O-D6        |
         |+++++++++++++           |
         |O-E1, O-E2, O-E3        |
         |-------------           |
         |O-E4, O-E5, O-E6        |                    
         =========================='''

    seats = {"DONT DELETE": {"Economy": {"Seats": 30, "Selection": bp},
                             "AC Lower": {"Seats": 30, "Selection": bp},
                             "AC Business": {"Seats": 30, "Selection": bp}}}

    @classmethod
    def set_seats(cls):

        for key, values in Management.trains.items():
            for class_, seat_ in values["Available Classes"].items():
                cls.seats[key] = {class_: {"Seats": seat_['Seats'], "Selection": cls.bp}}

    @classmethod
    def update_seats(cls, current_string: str, seats: list):

        for seat in seats:
            current_string = re.sub(fr"O-{seat}", f"X-{seat}", current_string)

        return current_string

    @classmethod
    def book_seats(cls, train_id: str, train_class_: str, seats_: int):
        seats_taken = 0

        displayed_blueprint = cls.seats[train_id][train_class_]["Selection"]

        print(displayed_blueprint)
        selected_seats = []

        while seats_taken != seats_:
            select_seat = input(F"\t (Type 'quit' to go back) {seats_taken + 1}. Choose your seat: ")
            if select_seat in displayed_blueprint:

                # check if it is chosen or not:
                if re.compile(fr"X-{select_seat}").search(displayed_blueprint) or select_seat in selected_seats:
                    print("\t Seat is already chosen, please select another seat.")

                else:
                    selected_seats.append(select_seat)
                    seats_taken += 1

            elif select_seat == "quit":
                break

            else:
                print("\t Enter a valid seat number.")

        if len(selected_seats) == seats_:
            updated_seats = cls.update_seats(cls.seats[train_id][train_class_]["Selection"], selected_seats)
            cls.seats[train_id][train_class_]["Selection"] = updated_seats
            return True, selected_seats

        else:
            return False, None
