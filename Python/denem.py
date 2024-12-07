class Product:
    def __init__(self,name="Default", price=0, quantity=1):
        print(f"An istance with name: {name} has been derived to {quantity} from price: {price} Product class.")
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def quantity(self):
        return self.__quantity
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @price.setter
    def price(self, value):
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
   
    def get_total_price(self):
        return self.__price * self.__quantity



item1 = Product("Laptop",799.90,2)
item1.name = "HP Laptop"
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.get_total_price())

item2 = Product()

item2.__name = "Computer"
item2.__price = 1999.99
item2.__quantity = 3

print(item2.name)
print(item2.price)
print(item2.quantity)
print("\n")

item3 = Product("Keyboard",25.99)
print(item3.name)
print(item3.price)
print(item3.quantity)
