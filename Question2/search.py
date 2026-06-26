# Linear Search
def linear_search(transaction_list, target_id):

    for transaction in transaction_list:
        if transaction.transaction_id == target_id:
            return transaction

    return None

# Binary Search (Recursive)
# Search transaction by transaction ID
def binary_search(transaction_list, target_id, left, right):
    # Base Case
    if left > right:
        return None

    # Find the middle index
    middle = (left + right) // 2

    # Transaction found
    if transaction_list[middle].transaction_id == target_id:
        return transaction_list[middle]

    # Search left half
    elif target_id < transaction_list[middle].transaction_id:
        return binary_search(transaction_list, target_id, left, middle - 1)

    # Search right half
    else:
        return binary_search(transaction_list, target_id, middle + 1, right)