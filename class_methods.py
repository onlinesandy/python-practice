class Car():
    """
    class documentation
    """
    def __init__(self,name="BMW",model="2020",price="25000000"):
        self.name = name
        self.model = model
        self.price = price

    def priceIncrease(self):
        print(type(self.price))
        self.price = int(self.price) + 1500

c = Car()

print(c.price)
c.priceIncrease()
print(c.price)

