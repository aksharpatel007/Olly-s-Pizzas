# Olly's Pizzas 🍕

A Python program to manage pizza orders for **Olly’s Pizzas**.  
This project demonstrates **object-oriented programming (OOP)** concepts such as classes, methods, and custom exceptions.

---

## 📌 Features
- **Pizza Class**
  - Supports three sizes: `small`, `medium`, `large`.
  - Supports multiple toppings: `corn`, `tomato`, `onion`, `capsicum`, `mushroom`, `olives`, `broccoli`.
  - Supports multiple cheeses: `mozzarella`, `feta`, `cheddar`.
  - Calculates price based on:
    - Size: `small = 50`, `medium = 100`, `large = 200`.
    - Toppings: `20` each, except `broccoli`, `olives`, `mushroom` which cost `50` each.
    - Cheese: `50` each.
  - Throws a **custom exception** (`InvalidChoiceError`) if an invalid size, topping, or cheese is selected.

- **Order Class**
  - Stores customer details (`name`, `customerid`).
  - Allows customers to order multiple pizzas in one order.
  - Generates a detailed bill showing each pizza’s configuration and total cost.

---

## 🛠️ How to Run
1. Save the program as `pizzeria.py`.
2. Run the program in terminal:
   ```bash
   python pizzeria.py
