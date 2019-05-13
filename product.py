class Product: 

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def __str__(self):
        return ("Your product: {}.".format(self.name))

    def calculate(self):
        total_price = self.base_price * self.tax_rate
        return total_price
        
