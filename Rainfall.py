num_years = int(input("Enter number of years: "))
rain_tracker = []

for i in range(1, num_years + 1):
    print("Year {}".format(i))
    for month in range(1, 13):
        rainfall = int(input("Enter amount of rainfall in inches for Month {}: ".format(month)))
        rain_tracker.append(rainfall)

months = num_years * 12
total_rainfall = sum(rain_tracker)
average_rainfall = total_rainfall / months

print("\nNumber of months:", months)
print("Total rainfall: {} inches".format(total_rainfall))
print("Average rainfall per month for the entire period: {:.2f}".format(average_rainfall))


