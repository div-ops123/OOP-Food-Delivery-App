# 🍔 OOP Food Delivery App (Python)

This is a simple **Object-Oriented Programming (OOP)** project simulating an online food delivery system, built as a learning exercise.

It demonstrates:
- Class design & relationships
- Clean project structure
- Inheritance, encapsulation, polymorphism, and abstraction
- Real-world modeling: users, restaurants, orders, payments, deliveries

---

## 📁 Project Structure

```text
online_food_delivery_app/
│
├── main.py # Entry point
├── models/ # All data models
│ ├── user.py # User, PremiumUser, VerifiedUser
│ ├── restaurant.py # Restaurant class
│ ├── order.py # Order class
│ ├── payment.py # Payment classes (PayPal, CreditCard)
│ └── logger.py # Logger mixin
│
├── services/ # Business logic layer
│ ├── order.py # apply_discount()
│ └── delivery.py # DeliveryUser logic
│
└── tests/ # Placeholder for unit tests
```

---

## ✅ Features

- 👤 Create premium users and verified users
- 🧾 Place orders from a restaurant
- 💳 Pay using different payment methods
- 🚚 Deliver orders using `DeliveryUser`
- 🎁 Apply tiered discounts
- 🧠 Follows best practices in OOP Python

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/div-ops123/OOP-Food-Delivery-App.git

cd OOP-Food-Delivery-App

# Run the main file
python main.py
```

---

## 🛠 Future Improvements

* [ ] Add unit tests using `pytest`
* [ ] Connect to real menus via API
* [ ] Add order history and delivery tracking

---

## 📚 Learning Goal

This project was built to **practice and master Python OOP principles** using a realistic use-case that simulates how apps like UberEats or Jumia Food work behind the scenes.

---

## 📸 Sample Output

```
[LOG]: divine is verified.
Total: 25
Discounted total: 20.0
Paid $ 20.0 using credit card ending in 3456
Delivering divine order (['Pizza', 'Burger']) to LA...
```
