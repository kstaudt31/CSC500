
#Build the ItemToPurchase class with the following specifications: Name, Price, Quantity, Description
class ItemToPurchase:

    #Constructor
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    #Method to get items cost and print the output
    def print_item_cost(self):
        totalCost = self.price * self.quantity
        print("{} {} @ ${:.0f} = ${}".format(self.name, self.quantity, self.price, int(totalCost)))

    #Method to get item description and output
    def print_item_description(self):
        print("{}: {}".format(self.name, self.description))

#Build the ShoppingCart class with the following specifications: Customer Name, Current Date, Empty Cart
class ShoppingCart:

    #Constructor
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    #Method to add item to cart, will build in Module 8
    def add_item(self, ItemToPurchase):
        pass

    # Method to remove item from cart, will build in Module 8
    def remove_item(self, item_name):
        pass

    # Method to modify item in cart, will build in Module 8
    def modify_item(self, ItemToPurchase):
        pass

    # Method to get quantity of all items in cart
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.quantity
        return total_items

    # Method to get total of all items in cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_item = item.quantity * item.price
            total_cost += total_item
        return total_cost

    # Method to print total of the cart
    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        total_items = self.get_num_items_in_cart()
        print("Number of items: {}".format(total_items))
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print("Total: ${:.0f}".format(total_cost))

    # Method to print the descriptions of each item
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

#Declare print menu function
def print_menu(shopping_cart):

    choice = ""

    #print menu
    while choice != "q":
        print("\nMenu")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option: ", end="")


        #get user input and change character inputted to lowercase
        choice = input().lower()
        print()

        #if choice is i output item descriptions
        if choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        # if choice is o output entire shopping cart
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

        # if choice is q then exit the while loop
        elif choice == "q":
            break

        # invalid input is ignored
        else:
            continue

def main():
    shopping_cart = ShoppingCart()

    #Added examples as add function is not supposed to be completed yet
    item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
    item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
    item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")

    shopping_cart.cart_items.append(item1)
    shopping_cart.cart_items.append(item2)
    shopping_cart.cart_items.append(item3)

    print_menu(shopping_cart)

if __name__ == "__main__":
    main()






