from .logger import Logger

class User:
    def __init__(self, username: str, address: str):
        self.username = username
        self.address = address

    def view_profile(self):
        return f"{self.username} address is {self.address}"
    

# Multi-Level Inheritance
class PremiumUser(User):
    def get_discount(self):
        return 0.10 # 10%
    
class PremiumGoldUser(PremiumUser):
    def get_discount(self):
        return 0.20 # 20%
    

class VerifiedUser(User, Logger):
    def verify_identity(self):
        # .log() returns None — it only prints to console
        # thus, don’t wrap it inside a return. Let .log() handle output
        self.log(message=f'{self.username} is verified.')         

                   