
#Ask the user to input the subtotal of the food
subtotal = float(input('Enter the subtotal of the bill: '))

#Create a variable and multiply the subtotal by .18 to get the tip and output
tip = subtotal * .18
print('\nThe tip amount is: ${:.2f}'.format(tip))

#Create a variable and multiply the subtotal by .07 to get the sales tax and output
salesTax = subtotal * .07
print('The sales tax amount is: ${:.2f}'.format(salesTax))

#Add the subtotal, tip, and sales tax, and output to get the total price
total = subtotal + tip + salesTax
print('\nThe total amount is: ${:.2f}'.format(total))