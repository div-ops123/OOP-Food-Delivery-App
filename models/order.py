from .user import User
from .restaurant import Resturant

# Encapsulation
class Order:
    def __init__(self, customer: User, resturant: Resturant, items: list):
        self.customer = customer
        self.resturant = resturant
        self.items = items
        self.__total = sum(resturant.menu[item] for item in items)  # Get the price of each item orders and sum it up.

    def get_total(self):
        return self.__total
    
