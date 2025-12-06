  # Custom Exception
class InvalidChoiceError(Exception):
    pass

class Pizza:
    # Allowed options
    sizes = {"small": 50, "medium": 100, "large": 200}
    toppings = {"corn": 20, "tomato": 20, "onion": 20, "capsicum": 20,
                "mushroom": 50, "olives": 50, "broccoli": 50}
    cheeses = {"mozzarella": 50, "feta": 50, "cheddar": 50}

    def __init__(self, size, toppings, cheeses):
        # Validate size
        if size.lower() not in Pizza.sizes:
            raise InvalidChoiceError(f"Size '{size}' not available.")
        self.size = size.lower()

        # Validate toppings
        for t in toppings:
            if t.lower() not in Pizza.toppings:
                raise InvalidChoiceError(f"Topping '{t}' not available.")
        self.toppings = [t.lower() for t in toppings]

        # Validate cheeses
        for c in cheeses:
            if c.lower() not in Pizza.cheeses:
                raise InvalidChoiceError(f"Cheese '{c}' not available.")
        self.cheeses = [c.lower() for c in cheeses]

    def price(self):
        cost = Pizza.sizes[self.size]
        for t in self.toppings:
            cost += Pizza.toppings[t]
        for c in self.cheeses:
            cost += Pizza.cheeses[c]
        return cost

    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings}, cheeses={self.cheeses}, price={self.price()})"


class Order:
    def __init__(self, name, customerid):
        self.name = name
        self.customerid = customerid
        self.pizzas = []

    def order(self):
        num = int(input("How many pizzas would you like to order? "))
        for i in range(num):
            print(f"\n--- Pizza {i+1} ---")
            size = input("Enter size (small/medium/large): ")

            toppings = input("Enter toppings separated by space: ").split()
            cheeses = input("Enter cheeses separated by space: ").split()

            try:
                pizza = Pizza(size, toppings, cheeses)
                self.pizzas.append(pizza)
                print("Pizza added successfully!")
            except InvalidChoiceError as e:
                print("Error:", e)

    def bill(self):
        print("\n========== BILL ==========")
        total = 0
        for i, pizza in enumerate(self.pizzas, start=1):
            print(f"Pizza {i}: {pizza}")
            total += pizza.price()
        print("----------------------------")
        print(f"Customer: {self.name} (ID: {self.customerid})")
        print(f"TOTAL COST: Rs.{total}")
        print("============================")


# Example Run
if __name__ == "__main__":
    print("Welcome to Olly's Pizzas!")
    name = input("Enter your name: ")
    cid = input("Enter customer ID: ")

    order = Order(name, cid)
    order.order()
    order.bill()
