#  Abstraction & Polymorphism: Payment Interface
from abc import ABC, abstractmethod

# Base class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# Create Class for each Payment method
class CreditCard(PaymentMethod):
    def __init__(self, card_number: str):
        self.__card_number = card_number

    def pay(self, amount):
        return f"Paid $ {amount} using credit card ending in {self.__card_number[-4:]}"  # I tought access required getters and setter
    
class PayPal(PaymentMethod):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount):
        return f"Paid $ {amount} using PayPal ({self.email})"