from models import Resturant, PremiumGoldUser, Order, CreditCard, VerifiedUser
from services import apply_disount, DeliveryUser


menu = {"Burger": 10, "Pizza": 15}
restaurant = Resturant("Mama Put", menu)
user = PremiumGoldUser("divine", "LA")
order = Order(user, restaurant, ["Pizza", "Burger"])
deliver_order = DeliveryUser(user.username, user.address)
payment_method = CreditCard("1234567890123456")
is_user_verified = VerifiedUser(user.username, user.address)

is_user_verified.verify_identity()
discounted_total = apply_disount(order=order, user=user)
total = order.get_total()
print(f"Total: {total}")
print(f"Discounted total: {discounted_total}")
print(payment_method.pay(discounted_total))
print(deliver_order.deliver(order))
