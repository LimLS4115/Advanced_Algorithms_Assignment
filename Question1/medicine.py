class Medicine:
    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    # Define how a medicine object is displayed
    def __str__(self):
        return(f"{self.medicine_id} {self.name} {self.category} {self.price} {self.quantity}")