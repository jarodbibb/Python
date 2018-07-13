import manage
class Product(object):
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.store = "none"
    
    def add_tax(self, percent):
        return self.price + (1 * (self.price *  percent))
if __name__ == "__main__":
    product = Product(18, "toy")
    print product.name
    print product.add_tax(0.18)
    

spoon = Product(13, "spoon")

print spoon.price


    