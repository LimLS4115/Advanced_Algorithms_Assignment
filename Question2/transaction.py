# Transaction Class
# Represents a customer transaction in an online shopping system

class Transaction:

    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    # Display transaction information
    def __str__(self):
        return (f"{self.transaction_id:<8}"
                f"{self.customer_name:<20}"
                f"{self.product_name:<15}"
                f"RM {self.amount:<12.2f}"
                f"{self.transaction_date:<12}")