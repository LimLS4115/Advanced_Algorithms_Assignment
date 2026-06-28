from multithreading import run_multithreading
from sequential import run_sequential

# Test the multithreading version for 10 rounds
def test_multithreading():
    print("\n===== Multithreading =====")

    total = 0

    for round_number in range(1, 11):

        time_taken = run_multithreading()
        total += time_taken

        print(f"Round {round_number:<3}: {time_taken:>7} ns")

    # Calculate the average execution time
    average = total / 10
    print("\nAverage Time:", average, "ns")

# Test the sequential version for 10 rounds
def test_sequential():

    print("\n===== Sequential =====")

    total = 0

    for round_number in range(1, 11):

        time_taken = run_sequential()
        total += time_taken

        print(f"Round {round_number:<3}: {time_taken} ns")

    # Calculate the average execution time
    average = total / 10

    print("\nAverage Time:", average, "ns")

def main():
    test_multithreading()
    print()
    test_sequential()

if __name__ == "__main__":
    main()