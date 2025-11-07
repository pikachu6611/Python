class Coffee:
    #initialize coffee with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    #initialize order with empty list
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order")

    def total(self):
        return sum(items.price for items in self.items)

    #show order summary

    def show_order(self):
        if not self.items:
            print("No items in the order")
            return
        print("\n Your order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} = Rs.{item.price}")

        print(f"Total: Rs.{self.total()}\n")

    #handle checkout processs
    def checkout(self):

        if not self.items:
            print("Your cart is empty")
            return

        self.show_order()
        confirm = input("Proceed to checkout? yes/no").lower()
        if confirm == "yes":
            print("Order confirmed. Thank you")
            self.items.clear()
        else:
            print("Order cancelled. Thank you")

#display menu and handle user input

def main():
    menu = [
        Coffee("Espresso", 250),
        Coffee("Latte", 350),
        Coffee("Cappuccino", 350),
        Coffee("Americano", 400)
    ]

    order = Order()

    while True:
        print("\n --- Coffee Menu --- ")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - Rs.{coffee.price}")

        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option ")
        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) -1])

        elif choice ==  '5':
            order.show_order()
        elif choice == '6':
            order.checkout()
        elif choice == '7':
            print("Thanks for visiting. Goodbye")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()
