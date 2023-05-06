# Ticket Booking System with Python Using if-elif-else ladder.
# Made By : Satvik Sharma (Data Science Trainee @ WS Cube Tech, Jaipur)
# Mentor Name : Miss Ayushi Jain 
# ------------------------------------------------------------- # 

# Welcome
while True:
    a = input("Please type hi to book your tickets:")
    if a == "hi":
        print("Welcome to inox theatres")
    else:
        print("Invalid Input")
        continue

# Select Your Location
    print("Please select your location:")
    location = [" kota", "jaipur", "delhi", "mumbai"]
    for i in location:
        print(i)

    city = input("Please enter your location:")
    if city == "kota":
        print("Welcome to inox, Ahluwalias the Great Mall")
    elif city == "jaipur":
        print("Welcome to INOX WTP Jaipur")
    elif city == "delhi":
        print("Welcome to INOX Nehru Nagar")
    elif city == "mumbai":
        print("Welcome to INOX Andheri [West]")
    else:
        print("We are not currently serving in your city.")

# Select Date and Time
    date = input("Please enter the date in which you want to watch the movie:")
    print("Available show timings are: 12:00pm , 3:00pm , 6:00pm ,9:00pm")

    time = input("Please enter the time:")
    print("Movies now showing are:")
    movie = ["Drishyam 2", "Pathan", "3 idots", "Jersey"]
    for i in movie:
        print(i)

# Select Your Movie To Watch
    a = input("Please type your movie name:")
    if a in ["Drishyam 2", "Pathan", "3 idots", "Jersey"]:
        print("Please select your seat")
        print("Available options are:")
        seat = ["silver:180", "gold: 250", "diamond:450", "recliner: 650"]
        for x in seat:
            print(x)

# Select Your Seat Preference
        a = input("Please type your seat type:")
        b = int(input("how many seats do you want:"))

        if a == "silver":
            s = 180 * b
            print("The total price for your ticket is ", s)
        elif a == "gold":
            s = 250 * b
            print("The total price for your ticket is ", s)
        elif a == "diamond":
            s = 450 * b
            print("The total price for your ticket is ", s)
        elif a == "recliner":
            s = 650 * b
            print("The total price for your ticket is ", s)
        else:
            print("Invalid Input")
            continue

# Add Ons 
        combo = input("Do you want to add any combo [Y/n]:")
        if combo == 'Y':
            print(""" Available Combos 
            1. Popcorn = 200
            2. Popcorn + Coke = 400 """
                  )
            l = input("Please enter your choice:")
            if l == "1":
                s += 200
                print("Our total bill is", s)
            elif l == "2":
                s += 400
                print("Our total bill is", s)
            else:
                print("Invalid Input")
                continue

# Exit
        print("Thank you for booking with us!")
    else:
        print("Invalid Input")
        continue

# Another Try 
    another_ticket = input("Do you want to book another ticket? [yes/no]: ")
    if another_ticket.lower() == "yes":
        continue
    else:
        break