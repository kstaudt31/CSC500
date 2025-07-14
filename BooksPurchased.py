books_purchased = int(input("How many books did you purchase this month? "))

if books_purchased == 0 or books_purchased == 1:
    print("Points awarded: 0")
elif books_purchased == 2 or books_purchased == 3:
    print("Points awarded: 5")
elif books_purchased == 4 or books_purchased == 5:
    print("Points awarded: 15")
elif books_purchased == 6 or books_purchased == 7:
    print("Points awarded: 30")
elif books_purchased >= 8:
    print("Points awarded: 60")

