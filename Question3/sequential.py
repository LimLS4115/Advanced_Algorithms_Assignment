import time
from factorial import factorial

# Run factorial calculations without multithreading
def run_sequential():
    # Record the start time
    start_time = time.perf_counter_ns()

    # Calculate factorials one by one
    factorial(50)
    factorial(100)
    factorial(200)

    # Record the end time
    end_time = time.perf_counter_ns()
    # Calculate total execution time
    total_time = end_time - start_time

    return total_time