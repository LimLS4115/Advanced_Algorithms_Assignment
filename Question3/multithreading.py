import threading
import time
from factorial import factorial

# Function executed by each thread
def calculate(number):
    factorial(number)

# Run factorial calculations using multithreading
def run_multithreading():
    threads = []

    # Numbers to calculate
    numbers = [50, 100, 200]

    # Record the start time
    start_time = time.perf_counter_ns()

    # Create and start one thread for each number
    for number in numbers:
        thread = threading.Thread(target=calculate, args=(number,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Record the end time
    end_time = time.perf_counter_ns()
    # Calculate total execution time
    total_time = end_time - start_time

    return total_time