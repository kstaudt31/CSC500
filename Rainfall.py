#Ask the user to input the number of years
num_years = int(input("Enter number of years: "))

#Create a list to hold values
rain_tracker = []

#Outer for loop to iterate through the number of years
for i in range(1, num_years + 1):
    print("Year {}".format(i))

    # An inner for loop to iterate through all of the months in 1 year
    for month in range(1, 13):
        # Ask the user to input the number of inches of rain for a month 12 times
        rainfall = int(input("Enter amount of rainfall in inches for Month {}: ".format(month)))
        # Add each user's input to the list
        rain_tracker.append(rainfall)

#Create a month variable to calculate the number of months
months = num_years * 12
#Create a total rainfall variable to add each item in the list together
total_rainfall = sum(rain_tracker)
#Create an average rainfall variable to divide the total rainfall by the number of months
average_rainfall = total_rainfall / months

#Output the number of months
print("\nNumber of months:", months)
#Output total rainfall
print("Total rainfall: {} inches".format(total_rainfall))
#Output average rainfall per month
print("Average rainfall per month for the entire period: {:.2f}".format(average_rainfall))


