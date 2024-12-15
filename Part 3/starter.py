from abc import ABC, abstractmethod


# Singleton Inventory Manager
class InventoryManager:
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }
    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}...")
        return True

class CreditCard(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}...")
        return True


class Pizza(ABC):
    def __init__(self):
        self.topping_manager = ToppingManager()
        self.description = ""
        self.cost = 0.0

    def addToppings(self, topping):
        self.topping_manager.addToppings(topping)

    def get_description(self):
        return self.description + self.topping_manager.get_description()

    def get_cost(self):
        return self.cost + self.topping_manager.get_cost()



class ToppingManager:
    def __init__(self):
        self.toppings = []

    def addToppings(self, topping):
        self.toppings.append(topping)

    def get_description(self):
        topping_string = ''
        for topping in self.toppings:
            topping_string += ", " + topping.get_description()  
        return topping_string

    def get_cost(self):
        total_cost = 0
        for topping in self.toppings:
            total_cost += topping.get_cost()  
        return total_cost



class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni"
        self.cost = 6.0

class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita"
        self.cost = 5.0
class Toppings(ABC):
    def get_description(self):
            pass
    def get_cost(self):
        pass

class cheese(Toppings):
    def __init__(self):
        self.description = "Cheese"
        self.cost = 1.0
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class cheese(Toppings):
    def __init__(self):
        self.description = "Cheese"
        self.cost = 1.0
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class olives(Toppings):
    def __init__(self):
        self.description = "Olives"
        self.cost = 0.9
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class mushroom(Toppings):
    def __init__(self):
        self.description = "Mushroom"
        self.cost = 0.7
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class PizzaFactory:
    @staticmethod
    def get_pizza(pizza_type):
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        return None
class ToppingFactory:
    @staticmethod
    def get_topping(topping_type):
        if topping_type == "Cheese":
            return cheese()
        elif topping_type == "Olives":
            return olives()
        elif topping_type == "Mushrooms":
            return mushroom()
        return None



# Main Function
def main():
    inventory_manager = InventoryManager()


    print("Welcome to the Pizza Restaurant!")


    while True:

        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        pizza =  None
        if pizza_choice == '0':
            break
        if pizza_choice == '1':
            pizza = PizzaFactory.get_pizza("Margherita")
        elif pizza_choice == '2':
            pizza = PizzaFactory.get_pizza("Pepperoni")
        else:
            print("Choose one of the available pizza types")
            continue
    

        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")
            # TODO: fill the following as required
            # Cheese
            if topping_choice == "1" :
                if inventory_manager.check_and_decrement("Cheese"):  # Check if Cheese is available
                    topping = ToppingFactory.get_topping("Cheese")
                    pizza.addToppings(topping)
            # Olive
            elif topping_choice == "2":
                if inventory_manager.check_and_decrement("Olives"):  # Check if Olives are available
                    topping = ToppingFactory.get_topping("Olives")
                    pizza.addToppings(topping)
            # Mushrooms
            elif topping_choice == "3":
                if inventory_manager.check_and_decrement("Mushrooms"):  # Check if Mushrooms are available
                    topping = ToppingFactory.get_topping("Mushrooms")
                    pizza.addToppings(topping)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

                   
                
                

        while True:
                print("\nAvailable Payment Methods:")
                print("1. PayPal")
                print("2. Credit Card")
                payment_choice = input("Enter the number of your choice: ")
           
                if payment_choice == "1":
                    payment_method = PayPal()
                    if payment_method.process_payment(pizza.get_cost()):
                         print("Payment successful via PayPal!")
                    break
                elif payment_choice == "2":
                    payment_method = CreditCard()
                    if payment_method.process_payment(pizza.get_cost()):
                        print("Payment successful via Credit Card!")
                    break
                elif payment_choice == "0":
                    print("Order cancelled.")
                    break
                else:
                    print("choose a valid method.")
           
        # Display final pizza details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Show final inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
