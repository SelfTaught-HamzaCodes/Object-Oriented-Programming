from RMS.Guest_UI import Guest


class User(Guest):

    @staticmethod
    def cli_helper(user=False):
        Guest.cli_helper(user)


if __name__ == "__main__":
    Guest.cli_helper(user=True)
