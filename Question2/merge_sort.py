# Merge Sort (Divide and Conquer)
# Count the number of recursive calls
recursive_calls = 0

# Merge two sorted lists into one sorted list
def merge(left, right):
    merged = []
    i = 0
    j = 0

    # Compare both lists and insert the smaller value
    while i < len(left) and j < len(right):

        if left[i].transaction_id < right[j].transaction_id:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Insert remaining elements from left list
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Insert remaining elements from right list
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# Merge Sort using Divide and Conquer
def merge_sort(transaction_list):
    global recursive_calls
    recursive_calls += 1

    # Base Case
    if len(transaction_list) <= 1:
        return transaction_list

    # Divide
    middle = len(transaction_list) // 2

    left_half = transaction_list[:middle]
    right_half = transaction_list[middle:]

    # Conquer
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combine
    return merge(left_half, right_half)

# Reset recursive counter
def reset_recursive_calls():
    global recursive_calls
    recursive_calls = 0

# Return total recursive calls
def get_recursive_calls():
    return recursive_calls