
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

    #Method to add item to cart
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # Method to remove item from cart
    def remove_item(self, item_name):

        #For loop to look for item in cart
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    #Method to modify item in cart
    def modify_item(self, item_to_modify):

        #For loop to look for item in cart
        for item in self.cart_items:
            if item.name == item_to_modify.name:
                item.quantity = item_to_modify.quantity
                return
        print("Item not found in cart. Nothing modified.")

    #Method to get quantity of all items in cart
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.quantity
        return total_items

    #Method to get total of all items in cart
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
        print("Number of Items: {}".format(total_items))
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print("Total: ${}".format(int(total_cost)))

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

        #if choice is i, output item descriptions
        if choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        #if choice is o, output entire shopping cart
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

        #if choice is q then exit the while loop
        elif choice == "q":
            break

        #if choice is a, add item to cart
        elif choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))

            #Create another instance of the item as your adding an item
            item = ItemToPurchase(name, price, quantity, description)

            #Add item to the cart
            shopping_cart.add_item(item)

        #if choice is r, remove item from cart
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(item_name)

        #if choice is c, change item quantity in cart
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))

            #Modify item quantity
            item = ItemToPurchase(name = name, quantity = quantity)
            shopping_cart.modify_item(item)

        # invalid input is ignored
        else:
            continue

def main():

    # Ask User for name and date
    customer_name = input("Enter customer's name:\n")
    today_date = input("Enter today's date:\n")

    #Print name and date
    print("\nCustomer name: {}".format(customer_name))
    print("Today's date: {}".format(today_date))

    #Create instance
    shopping_cart = ShoppingCart(customer_name, today_date)

    #Print menu
    print_menu(shopping_cart)

if __name__ == "__main__":
    main()






