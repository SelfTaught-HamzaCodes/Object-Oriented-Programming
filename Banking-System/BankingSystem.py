# Project: Banking System

class Registration:

    def __init__(self, name: str, age: int, gender: str):

        # Initializing our values:
        self.__name = name
        self.__age = age
        self.__gender = gender

    # Encapsulation: The name attribute cannot be directly accessed, it can only be accessed or changed through the
    # methods.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def show_details(self):
        return (F'''Personal Details

Name: {self.__name},
Age: {self.__age},
Gender: {self.__gender} ''')


# Inheritance: Class Bank Inherits Methods and Attributes from Registration.
class Bank(Registration):

    # Keeping Track of All Users:
    __users = 0
    __total_deposits = 0

    # Add Customer, update total users and balance.
    def __init__(self, name, age, gender, balance=0):
        super().__init__(name, age, gender)
        self.__balance = balance

        Bank.__users += 1
        Bank.__total_deposits += self.__balance

    # Deposit Amount:
    def deposit(self, amount):
        self.__balance += amount
        Bank._calculate_total_deposits(amount, credit=True, authorized=True)
        return F"Amount balance has been updated to: ${self.__balance}"

    # Withdraw Amount:
    def withdraw(self, amount):

        if self.__balance < amount:
            return F"Insufficient funds to withdraw ${amount}, You have: ${self.__balance}"
        else:
            self.__balance -= amount
            Bank._calculate_total_deposits(amount, debit=True, authorized=True)
            return F"Withdrawal complete for ${amount}, remaining balance ${self.__balance}"

    # Customer Balance:
    def view_balance(self):
        return F"{self.name} you have ${self.__balance} in your account!"

    @classmethod
    def _calculate_total_deposits(cls, amount, credit=False, debit=False, authorized=False):

        if authorized:
            if credit:
                Bank.__total_deposits += amount

            elif debit:
                Bank.__total_deposits -= amount

        else:
            return "You are not authorized to view this information"

    @classmethod
    def _user(cls, authorized=False):
        if authorized:
            return cls.__users, cls.__total_deposits
        else:
            return "You are not authorized to view this information"


# Inheritance: Class Admin Inherits Methods and Attributes from Bank.
class Admin(Bank):

    @classmethod
    def current_users(cls):
        users, deposits = cls._user(authorized=True)
        return F"Number of users are: {users} | Total Deposits ${deposits}"


def main():

    # Adding customers by creating bank objects:
    person1 = Bank("Matt", 21, "M")
    person2 = Bank("Emily", 27, "F")
    person3 = Bank("Jason", 45, "M")
    person4 = Bank("Bill", 58, "M")

    # Revise name of customer:
    person4.name = "Billy"

    # Display details:
    print(person4.show_details())

    print()

    # Deposit less, withdraw more:
    person1.deposit(500)
    print(person1.withdraw(750))  # Error

    print()

    # Deposit amount:
    person2.deposit(500)
    person3.deposit(1000)
    person4.deposit(200)

    # Deny unauthorized access:
    print(person4._calculate_total_deposits(500))

    print()

    # Administration:
    print(Admin.current_users())


main()
