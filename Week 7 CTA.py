room_dict = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructor_dict = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

time_dict = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

user_course = input("Enter a course number or 'q' to quit: ")

while user_course != 'q': 
    if user_course in room_dict:
        room_number = room_dict[user_course]
        instructor = instructor_dict[user_course]
        meeting_time = time_dict[user_course]
        print(user_course, "is taught at room",room_number, "by professor", instructor, "at", meeting_time)
    else:
        print("Course not found.")
    print("\n")
    user_course = input("Enter a course number or 'q' to quit: ")