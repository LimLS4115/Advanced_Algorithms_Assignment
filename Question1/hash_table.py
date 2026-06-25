# Hash Table Class using Linear Probing
class HashTable:

    def __init__(self, size):
        self.size = size            # Size of hash table
        self.table = [None] * size  # Create empty buckets

    def hash_function(self, key):
        number = (int(key[1:]) * 31)       # Convert M001 -> 001 -> 1
        return number % self.size   # Calculate index position

    def insert(self, medicine):

        # Find initial index using hash function
        index = self.hash_function(medicine.medicine_id)

        # Move to next bucket if current bucket is occupied
        while self.table[index] is not None:
            index = (index + 1) % self.size

        # Insert medicine into empty bucket
        self.table[index] = medicine

    def search(self, medicine_id):

        # Calculate starting position
        index = self.hash_function(medicine_id)

        # Continue searching until an empty bucket is found
        while self.table[index] is not None:

            # Record found
            if self.table[index].medicine_id == medicine_id:
                return self.table[index]

            # Check next bucket
            index = (index + 1) % self.size

        # Record not found
        return None

    def display(self):
        print("")
        print(f"{'Medicine List':^60}")
        print("-" * 60)
        print(f"{'ID':<6}{'Name':<20}{'Category':<15}{'Price':<10}{'Quantity':<15}")
        print("-" * 60)

        for item in self.table:

            if item is not None:
                print(f"{item.medicine_id:<6}{item.name:<20}{item.category:<15}{item.price:<10.2f}{item.quantity:<15}")

        print("-" * 60)