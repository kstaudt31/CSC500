
#Build the ItemToPurchase class with the following specifications: Name, Price, Quantity
class ItemToPurchase:

    #Constructor
    def __init__(self, name="none", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Method to get items cost and print the output
    def print_item_cost(self):
        totalCost = self.price * self.quantity
        print("{} {} @ ${} = ${}".format(self.name, self.quantity, self.price, int(totalCost)))

#Prompt user for two items and create two objects of the ItemToPurchase class
item1 = ItemToPurchase()
print("Item 1")
item1.name = input("Enter the item name:\n")
item1.price = float(input("Enter the item price:\n"))
item1.quantity = int(input("Enter the item quantity:\n"))

item2 = ItemToPurchase()
print("Item 2")
item2.name = input("Enter the item name:\n")
item2.price = float(input("Enter the item price:\n"))
item2.quantity = int(input("Enter the item quantity:\n"))

#Add the costs of the two items together and output the total cost
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
total = (item1.price * item1.quantity) + (item2.price * item2.quantity)
print("Total: ${}".format(int(total)))


