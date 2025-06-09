#========The beginning of the class========== 
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # Initialize the Shoe object with provided attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Return the cost of the shoe
        return self.cost 

    def get_quantity(self):
        # Return the quantity of the shoe
        return self.quantity

    def __str__(self):
        # Return a string representation of the shoe
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


#=============Shoe list===========
# List to store all Shoe objects
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    # Read shoe data from inventory.txt and populate the shoe_list
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip the header
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    # Capture a new shoe entry from user input and append it to shoe_list
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    # Append new shoe data to inventory.txt
    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")


def view_all():
    # Display all shoes in the inventory
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    # Find the shoe with the lowest quantity and offer to restock
    lowest = min(shoe_list, key=lambda x: x.quantity)
    print("Lowest stock:", lowest)
    add = input("Would you like to restock this item? (yes/no): ").lower()
    if add == "yes":
        try:
            add_qty = int(input("Enter quantity to add: "))
            lowest.quantity += add_qty
            # Rewrite the updated inventory back to the file
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        except ValueError:
            print("Invalid quantity input.")


def seach_shoe():
    # Search for a shoe using the shoe code
    code = input("Enter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")


def value_per_item():
    # Calculate and display total value of each shoe (cost * quantity)
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} - Value: {value}")


def highest_qty():
    # Find and display the product with the highest quantity
    highest = max(shoe_list, key=lambda x: x.quantity)
    print(f"{highest.product} is now on SALE! Quantity: {highest.quantity}")


#==========Main Menu=============
def main():
    # Main menu loop to execute functions based on user input
    read_shoes_data()
    while True:
        print("""
        ==== Shoe Inventory Menu ====
        1. View all shoes
        2. Capture new shoe
        3. Re-stock shoe
        4. Search shoe by code
        5. Calculate value per item
        6. Show product with highest quantity
        7. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            seach_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
