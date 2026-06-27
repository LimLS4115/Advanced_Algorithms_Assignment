# Calculate the factorial of a given number
def factorial(number):
    result = 1

    # Multiply all numbers from 1 to the given number
    for i in range(1, number + 1):
        result = result * i

    return result