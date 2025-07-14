#Ask the user to input the number of books purchased in a month
books_purchased = int(input("How many books did you purchase this month? "))

#An if statement for 0 or 1 books purchased and output points
if books_purchased == 0 or books_purchased == 1:
    print("Points awarded: 0")

#Else if statement for 2 or 3 books purchased and output points
elif books_purchased == 2 or books_purchased == 3:
    print("Points awarded: 5")

#Else if statement for 4 or 5 books purchased and output points
elif books_purchased == 4 or books_purchased == 5:
    print("Points awarded: 15")

#Else if statement for 6 or 7 books purchased and output points
elif books_purchased == 6 or books_purchased == 7:
    print("Points awarded: 30")

#Else if statement for 8 or more books purchased and output points
elif books_purchased >= 8:
    print("Points awarded: 60")

