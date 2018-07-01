class Store(object):
    def __init__(self, location, owner):
        self.product = []
        self.location = location
        self.owner = owner
    def add_product(self, prod):
        self.product.append(prod)
        return self
    def remove_product(self, prod):
        self.product.remove(prod)
        return self
    def print_p(self):
        for x in self.product:
            print x
        return ","
    def display(self):
        print "Owner: ", self.owner, "Products: ", self.print_p(), "location: ", self.location

new_store = Store( "san jose", "jarod")

new_store.add_product("tic tac").add_product("bike").display()

if __name__ == "__main__":
    print "21", new_store