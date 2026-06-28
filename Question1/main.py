import time

from medicine import Medicine
from hash_table import HashTable

# Sequential search in an array
def array_search(array, medicine_id):

    for medicine in array:
        if medicine.medicine_id == medicine_id:
            return medicine

    return None

def system_menu():
    print("\n======= Pharmacy Inventory System =======")
    print("[1] Display Medicines")
    print("[2] Insert Medicine")
    print("[3] Search Medicine")
    print("[4] Edit Medicine")
    print("[5] Performance Comparison")
    print("[0] Exit")

def validate_id(hash_table):
    valid = False

    while not valid:
        id = input("Medicine ID: M")

        if not id.isdigit():
            print("Please enter numbers only.")
        elif int(id) <= 0:
            print("ID must be greater than 0.")
        else:
            medicine_id = "M" + id
            result = hash_table.search(medicine_id)

            if result:
                print("Medicine ID already exists.")
            else:
                valid = True

    return medicine_id

def validate_name():
    name = input("Medicine Name: ").strip()

    while name == "":
        print("Medicine name cannot be empty.")
        name = input("Medicine Name: ").strip()

    return name

def validate_category():
    category = input("Category: ").strip()

    while category == "":
        print("Medicine category cannot be empty.")
        category = input("Category: ").strip()

    return category

def validate_price():
    valid = False

    while not valid:
        try:
            price = float(input("Price: RM "))

            if price <= 0:
                print("Price must be greater than 0.")
            else:
                valid = True

        except ValueError:
            print("Invalid price. Please enter numbers only.")

    return price

def validate_quantity():
    valid = False

    while not valid:
        quantity = input("Quantity: ")

        if not quantity.isdigit():
            print("Invalid quantity. Please enter a number greater than 0.")
        elif int(quantity) <= 0:
            print("Invalid quantity. Please enter a number greater than 0.")
        else:
            valid = True

    return int(quantity)

def insert_medicine(hash_table, medicine_array):

    print("Please enter medicine detail")

    medicine_id = validate_id(hash_table)
    name = validate_name()
    category = validate_category()
    price = validate_price()
    quantity = validate_quantity()

    medicine = Medicine(medicine_id, name, category, price, quantity)

    hash_table.insert(medicine)
    medicine_array.append(medicine)

    print("Medicine inserted successfully.")

def search_medicine(hash_table):
    id = input("Enter Medicine ID: M")

    if not id.isdigit():
        print("Invalid Medicine ID")
        return

    medicine_id = "M" + id

    result = hash_table.search(medicine_id)

    if result is None:
        print("\nMedicine not found.")
        return

    print("\nMedicine found.")
    print("Medicine ID:", result.medicine_id)
    print("Name:", result.name)
    print("Category:", result.category)
    print(f"Price: RM {result.price:.2f}")
    print("Quantity:", result.quantity)


def edit_medicine(hash_table):

    id = input("Enter Medicine ID: M")

    if not id.isdigit():
        print("Invalid Medicine ID")
        return

    medicine_id = "M" + id

    medicine = hash_table.search(medicine_id)

    if medicine is None:
        print("Medicine not found.")
        return

    choice = ""
    while choice != "5":
        print("\nChoose field to edit:")
        print("1. Name")
        print("2. Category")
        print("3. Price")
        print("4. Quantity")
        print("5. Back to Main Menu")
        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            print("Current name:", medicine.name)
            medicine.name = validate_name()
            print("Medicine name updated successfully.")

        elif choice == "2":
            print("Current category:", medicine.category)
            medicine.category = validate_category()
            print("Medicine category updated successfully.")

        elif choice == "3":
            print(f"Current price: RM {medicine.price:.2f}")
            medicine.price = validate_price()
            print("Medicine price updated successfully.")

        elif choice == "4":
            print("Current quantity:", medicine.quantity)
            medicine.quantity = validate_quantity()
            print("Medicine quantity updated successfully.")

        elif choice == "5":
            print("Back to main menu.")
            return

        else:
            print("\nInvalid Choice. Please enter number 1-5.")

def compare(hash_table, medicine_array):
    print("\n---------- Performance Comparison ----------")

    test_keys = [medicine.medicine_id for medicine in medicine_array]
    test_keys.append("M999")

    for key in test_keys:
        # Measure array search execution time
        # Record the start time
        start = time.perf_counter_ns()

        for i in range(10000):
            array_search(medicine_array, key)

        # Record the end time
        end = time.perf_counter_ns()

        # Calculate execution time
        array_time = end - start

        # Measure hash table search execution time
        start = time.perf_counter_ns()

        for i in range(10000):
            hash_table.search(key)

        end = time.perf_counter_ns()
        hash_time = end - start

        print(key, "| Array:", array_time, "ns", "| Hash:", hash_time, "ns")

def main():
    # Create Hash Table
    hash_table = HashTable(20)

    medicine_array = []

    # Sample Records
    sample_data = [
        Medicine("M001","Panadol","Tablet", 4.50, 100),
        Medicine("M002","Cetirizine","Tablet", 10.00, 60),
        Medicine("M003","Vitamin C","Supplement", 25.90, 80),
        Medicine("M004","Fish Oil","Supplement", 50.00, 40),
        Medicine("M005","Benadryl","Syrup", 40.00, 35),
        Medicine("M006", "Copastin", "Tablet", 5.50, 85),
        Medicine("M007", "Loratadine", "Tablet", 8.00, 20),
        Medicine("M008", "Dyriton", "Syrup", 13.20, 45),
        Medicine("M009", "Dyriton", "Tablet", 2.00, 30),
        Medicine("M010", "Paracil", "Tablet", 1.50, 120)
    ]

    for medicine in sample_data:
        hash_table.insert(medicine)
        medicine_array.append(medicine)

    # Pharmacy Inventory Menu
    choice = ""

    while choice != "0":
        system_menu() # Display menu
        choice = input("\nEnter your choice (1-5) or 0 to exit: ")

        if choice == "1":
            hash_table.display()
        elif choice == "2":
           insert_medicine(hash_table, medicine_array)
        elif choice == "3":
            search_medicine(hash_table)
        elif choice == "4":
            edit_medicine(hash_table)
        elif choice == "5":
            compare(hash_table, medicine_array)
        elif choice == "0":
            print("\nThank you for using the Pharmacy Inventory System.") # Exit
        else:
            print("\nInvalid Choice. Please enter number 0-5.")

if __name__ == "__main__":
    main()