
#Ask user to input the current time (in hours)
#Ask user to input the number of hours the alarm should wait before going off
#Use while loops to ensure proper inputs

while True:
    currentTime = int(input("Enter the current time (in hours): "))
    if currentTime < 24 and currentTime >= 0:
        break
    else:
        print("Sorry, the current time is out of range. Please use a number between 0 and 23")

while True:
    hoursWaiting = int(input("Enter the number of hours to wait until the alarm goes off(in hours):"))
    if hoursWaiting > 0:
        break
    else:
        print("Please enter a non-negative integer")


#Create variable and add the current time and the number of hours to wait
#Modulo the sum by 24

alarmTime = (currentTime + hoursWaiting) % 24

#Output the statement and answer
print("\nThe alarm will ring at {}".format(alarmTime))