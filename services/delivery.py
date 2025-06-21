'''Here's what this file is supposed to do:

Assign delivery person

Track delivery

Simulate delivery steps like “on the way”, “delivered”

You can define a DeliveryService class
'''
from models import User, Order

# Single Inheritance.
class DeliveryUser(User):   
    def deliver(self, order: Order):
        return f"Delivering {self.username} order ({order.items}) to {self.address}..."