from models import Order, User

# Substract the disocunt from the total
def apply_disount(order: Order, user: User) -> float:
    total = order.get_total()
    discount = user.get_discount()
    return total - (total * discount)
