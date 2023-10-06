## Banking System
A simple **Bank System** created in **Python**, primarily focusing on **Object-oriented Programming** and its principals.

#### Functionality:
- Add customers.
- Customers can deposit money.
- Customers can withdraw money.
- Adminstatrators can view total number of customers and the total amount of deposit.

#### Principals explored:
- **Inheritance**
  ```py
  # Inheritance: Class Bank Inherits Methods and Attributes from Registration.
  class Bank(Registration):
  ```
- **Encapsulation**
  ```py
  # Initializing our values:
  self.__name = name
  self.__age = age
  self.__gender = gender

  # Encapsulation: The name attribute cannot be directly accessed, it can only be accessed or changed through the methods.
  @property
  def name(self):
      return self.__name

  @name.setter
  def name(self, value):
      self.__name = value
  ```
***
Cheers,  
Muhammad Hamza Saeed.
