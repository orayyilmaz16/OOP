class Product(object):
    def __init__(self,name="Default", price=0, quantity=1) -> None:
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
    def name(self, value:str) -> None:
        self.__name = value
    
    @price.setter
    def price(self, value):
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
   
    def get_total_price(self) -> float:
        return self.__price * self.quantity

    def __repr__(self):
        return f"{self.__name} - {self.__price} - {self.__quantity}"

item1 = Product("Laptop",799.90,2)
item1.name = "HP Laptop"
print(item1)

item2 = Product("Computer")
item2.__price = 1999.99
item2.__quantity = 3
print(item2)

item3 = Product("Keyboard",25.99)
print(item3)