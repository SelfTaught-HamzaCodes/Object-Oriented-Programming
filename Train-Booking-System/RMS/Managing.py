class Management:
    # Class Variables:
    ticket_id = 1
    reference_number = "PRW-00001"

    # To store all tickets.
    # key = ticket_id | value = details
    tickets = {
        "DONT DELETE": {"First Name": "Test",
                        "Last Name": "Test",
                        "Age": 22,
                        "Identity Number": "00000-0000000-0",
                        "Contact Number": "0300-0000000",
                        "Departure City": "Karachi",
                        "Arrival City": "Lahore"}
    }

    # To store all trains.
    # key = train_id | value = details
    trains = {
        "DONT DELETE": {"Train Name": "Karachi Express",
                        "Train Source": "Karachi",
                        "Train Destination": "Lahore",
                        "Train Departure": "16:00",
                        "Train Arrival": "09:00",
                        "Available Classes": {"Economy": {"Price": 3_000, "Seats": 30},
                                              "AC Lower": {"Price": 5_000, "Seats": 30},
                                              "AC Business": {"Price": 8_000, "Seats": 30}}}
    }

    @classmethod
    def increment_reference(cls, reference=reference_number, t_id=0):
        length = len(str(t_id))
        reference = reference[:-length] + str(t_id)
        return reference

    @classmethod
    def find_train(cls, t_id):
        d = cls.tickets.get(t_id)["Departure City"]
        a = cls.tickets.get(t_id)["Arrival City"]

        available_trains = []

        for t_id, t_details in cls.trains.items():
            if t_details["Train Source"] == d and t_details["Train Destination"] == a:
                available_trains.append(t_id)

        if not len(available_trains):
            return False, F"No Trains available for -{d}- to -{a}-"

        else:
            return True, available_trains

