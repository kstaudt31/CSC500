
#Create a dictionary containing course numbers and the room numbers of the rooms where the courses meet
room_num = {
    "CSC101" : 3004,
    "CSC102" : 4501,
    "CSC103" : 6755,
    "NET110" : 1244,
    "COM241" : 1411
}

#Create a dictionary containing course numbers and the names of the instructors who teach each course
instructors = {
    "CSC101" : "Haynes",
    "CSC102" : "Alvarado",
    "CSC103" : "Rich",
    "NET110" : "Burke",
    "COM241" : "Lee"
}

#Create a dictionary containing course numbers and the meeting times of each course
time = {
    "CSC101" : "8:00 a.m.",
    "CSC102" : "9:00 a.m.",
    "CSC103" : "10:00 a.m.",
    "NET110" : "11:00 a.m.",
    "COM241" : "1:00 p.m."
}

#Get the course number from user input and capitalize the letters of the input so it always matches the key
course_num = input("Enter a course number or enter 'q' to quit: ").upper()

#Use a while loop to allow the user to look up as many classes as they would like, or enter 'q' to quit
while course_num != "Q":

    #Use an if statement to determine if the course number the user entered is in a dictionary
    if course_num in room_num:

        #Output room number, instructor, and meeting time of the course that the user inputted
        print("{}'s Room #: {}".format(course_num, room_num[course_num]))
        print("{}'s Instructor: {}".format(course_num, instructors[course_num]))
        print("{}'s Time: {}\n".format(course_num, time[course_num]))

    #Use the else statement to tell the user that the course number they input is not valid
    else:
        print("Invalid course number. Please enter a valid course number.\n")

    #Ask for user input again so the user can continue looking up courses
    course_num = input("Enter a course number or enter 'q' to quit: ").upper()