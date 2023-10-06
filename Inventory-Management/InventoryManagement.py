# Inventory Management:


class InventoryManagement:

    def __init__(self):
        self.inventory = {}  # Dictionary to hold inventory.
        self.products = 0  # Total Products.

    def add_item(self, name, cost, price, quantity, discount):
        """
        Add a product to the inventory.
        :param name: Product Name.
        :param cost: Product Cost.
        :param price: Product Price.
        :param quantity: Product Quantity.
        :param discount: Product Discount in % (if any).
        """

        # If product exists:
        if self.inventory.get(name, 0):
            print(f"{name} already exists.")

        # If product doesn't exist, add it to the inventory:
        else:
            self.inventory[name] = {
                "Cost": cost,
                "Price": price,
                "Quantity": quantity,
                "Discount": discount,
            }
            self.products += 1
            print(f"{name} was successfully added!")

    def modify_item(self, name):
        """
        Modify a product in the nventory.
        :param name: Product Name.
        """

        # If product in inventory:
        if self.inventory.get(name, 0):
            print("1- Name, 2- Cost, 3-Price, 4-Quantity, 5-Discount, 6-All")

            while True:
                choice = input(f"Which property of {name} would you like to change: ")

                # Assign new name:
                if choice == "1":
                    self.inventory[input(F"Change '{name}' to: ")] = self.inventory.pop(name)

                # Assign values to each field:
                elif choice == "6":
                    properties = input("Enter the details (Cost, Price, Quantity, Discount): ").split(", ")
                    self.inventory[name] = {
                        "Cost": int(properties[0]),
                        "Price": int(properties[1]),
                        "Quantity": int(properties[2]),
                        "Discount": int(properties[3]),
                    }

                # Assign values to specific field:
                else:
                    for index, inner_key in enumerate(self.inventory[name]):
                        if int(choice) == index + 2:
                            self.inventory[name][inner_key] = int(input(f"{inner_key}: "))
                            break

                break

        # If product not in inventory:
        else:
            print(f"{name} not found.")

    def delete_item(self, name):
        """
        Delete a product from inventory.
        :param name: Product Name.
        """

        # If product in inventory, take confirmation before removing the product.
        if self.inventory.get(name, 0):
            print(f"Item being deleted: {name}")
            choice = input("Are you sure ? Y/N: ")

            if choice == "Y":
                self.inventory.pop(name)
                self.products -= 1
                print(f"{name} was deleted successfully.")

            else:
                pass
        else:
            print(f"{name} not found.")


def main():

    # An instance of the Inventory Management System:
    ims = InventoryManagement()

    print("Inventory Management System")

    while True:

        user = input("""
Enter 1 to Add a product.
Enter 2 to Remove a product.
Enter 3 to Modify a product.
Enter 4 to View inventory.
Enter 5 to Quit.

: """)

        # Correct Option Selected:
        if user in [str(x) for x in range(1, 5)]:

            if user == "1":

                new_product = {
                    "Name": "",
                    "Cost": "",
                    "Price": "",
                    "Quantity": "",
                    "Discount": ""
                }

                # Get details of product:
                for key in new_product.copy():
                    new_product[key] = input(f"Set {key}: ")

                    if key == "Name":
                        if new_product["Name"] in ims.inventory:
                            break

                # Add product:
                ims.add_item(new_product["Name"],
                             new_product["Cost"],
                             new_product["Price"],
                             new_product["Quantity"],
                             new_product["Discount"])

            elif user == "2" or user == "3":

                product = input("Enter product: ")

                # Delete or Modify Product:
                if user == "2":
                    ims.delete_item(product)
                else:
                    ims.modify_item(product)

            else:

                print(f"Total Products: {ims.products}")
                print(ims.inventory)

        # In-Correct Option Selected:
        else:
            print("Choose a valid option.")


main()

