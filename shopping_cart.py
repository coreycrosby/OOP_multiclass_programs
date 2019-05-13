from product import Product

class ShoppingCart:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)
        return ("You have added {} to your cart.".format(product.name))

    def remove(self, product):
        self.products.remove(product)
        return ("You have removed {} from your cart.".format(product.name))

    def list_items(self):   
        output = [str(product) for product in self.products]
        return "\n".join(output)

    def total_before_tax(self):
        total = 0
        for product in self.products:
            total += product.base_price
        return total

    def total_after_tax(self):
        total = 0
        for product in self.products:
            total = total + (product.base_price * (1+product.tax_rate))
        return total


car = Product("Delorian", 1000000, 0.13)
bear = Product("Fortnite Bear", 100, 0.13)

cart = ShoppingCart()
cart.add(car)
cart.add(bear)
print(cart.total_before_tax())
print(cart.total_after_tax())
cart.remove(car)
print(cart.total_before_tax())
print(cart.total_after_tax())