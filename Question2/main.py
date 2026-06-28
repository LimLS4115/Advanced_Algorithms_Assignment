import time

from data import transactions
from merge_sort import merge_sort, reset_recursive_calls, get_recursive_calls
from search import binary_search, linear_search

# Display all transactions
def display_transactions(transaction_list):
    print(f"{'Transaction List':^70}")
    print("-" * 70)
    print(f"{'ID':<8}{'Customer':<20}{'Product':<15}{'Amount':<15}{'Date':<12}")
    print("-" * 70)

    for transaction in transaction_list:
        print(transaction)

    print("-" * 70)

# Display menu
def system_menu():
    print("\n======== Transaction Management System ========")
    print("[1] Display Transactions")
    print("[2] Merge Sort Transactions")
    print("[3] Binary Search")
    print("[4] Linear Search")
    print("[5] Performance Comparison")
    print("[0] Exit")

# Performance Comparison
def compare_performance():

    print("\n========== Performance Comparison ==========")

    # Merge Sort
    copy_list = transactions[:]

    reset_recursive_calls()

    start = time.perf_counter()
    sorted_list = merge_sort(copy_list)
    end = time.perf_counter()

    merge_time = end - start

    # Transaction ID used for performance testing
    target = 1006

    # Binary Search
    start = time.perf_counter()
    binary_search(sorted_list, target, 0, len(sorted_list) - 1)
    end = time.perf_counter()

    binary_time = end - start

    # Linear Search
    start = time.perf_counter()
    linear_search(sorted_list, target)
    end = time.perf_counter()

    linear_time = end - start

    print(f"Merge Sort Time   : {merge_time:.8f} seconds")
    print(f"Binary Search Time: {binary_time:.8f} seconds")
    print(f"Linear Search Time: {linear_time:.8f} seconds")
    print(f"Recursive Calls   : {get_recursive_calls()}")

    print("\nResult:")
    if binary_time < linear_time:
        print("Binary Search is faster than Linear Search.")
    else:
        print("Linear Search is faster than Binary Search.")

def main():
    sorted_transactions = transactions[:]
    is_sorted = False
    choice = ""

    while choice != "0":
        system_menu()
        choice = input("\nEnter your choice (1-5) or 0 to exit: ")

        if choice == "1":
            display_transactions(sorted_transactions)

        elif choice == "2":
            print("\nBefore Sorting")
            display_transactions(sorted_transactions)

            reset_recursive_calls()

            sorted_transactions = merge_sort(sorted_transactions)

            is_sorted = True

            print("\nAfter Sorting")
            display_transactions(sorted_transactions)

            print("\nRecursive Calls:", get_recursive_calls())

        elif choice == "3":

            if not is_sorted:
                print("\nPlease sort the transactions first.")
            else:
                target = input("Enter Transaction ID to search: ")

                if not target.isdigit():
                    print("Invalid ID. Please try again.")

                else:
                    target = int(target)

                    result = binary_search(sorted_transactions, target, 0, len(sorted_transactions) - 1)

                    if result:
                        print("\nTransaction found")
                        print("Transaction ID:", result.transaction_id)
                        print("Customer Name:", result.customer_name)
                        print("Product Name:", result.product_name)
                        print(f"Amount: RM {result.amount:.2f}")
                        print("Transaction Date:", result.transaction_date)

                    else:
                        print("\nTransaction not found")

        elif choice == "4":

            target = input("Enter Transaction ID to search: ")

            if not target.isdigit():
                print("Invalid ID. Please try again.")

            else:
                target = int(target)

                result = linear_search(transactions, target)

                if result:
                    print("\nTransaction found")
                    print("Transaction ID:", result.transaction_id)
                    print("Customer Name:", result.customer_name)
                    print("Product Name:", result.product_name)
                    print(f"Amount: RM {result.amount:.2f}")
                    print("Transaction Date:", result.transaction_date)

                else:
                    print("\nTransaction not found")

        elif choice == "5":
            compare_performance()

        elif choice == "0":
            print("\nThank you for using the Transaction Management System.")

        else:
            print("\nInvalid choice. Please enter number 0-5.")

if __name__ == "__main__":
    main()