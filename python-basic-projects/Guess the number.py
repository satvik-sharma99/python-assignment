a = input("Please type hello to play the game:")
if (a=="hello"):
    print("""Welcome to the game:"Can you guess my mind!" """)
    print("""Instructions for this game are very simple:
    1. You have to choose a number between 1-10
    2. Computer will also display a random number between 1-10
    3. If the number displayed by computer and your number gets match , you will win the game
    4. Note : For guessing the number you will get only 3 chances . 
    """)
print("Type 'Y' if you agree to the rules of game ")
s = input("Please enter your choice:")
if s=="Y":
    print("You can start the game ")

    while True:
        print("You have 3 chances")
        num1 = int(input("Enter your number:"))
        import random
        rand_No = random.randint(1,10)
        print("My number is: ",rand_No)
        if num1==rand_No:
            print("Bravo!, You are more smarter than me ")
        else:
            print("Bad luck! , Please try again")
        print("You have only  2 chances left")
        num1 = int(input("Enter your number:"))
        import random
        rand_No = random.randint(1,10)
        print("My number is: ",rand_No)
        if num1==rand_No:
            print("Bravo!, You are more smarter than me ")
        else:
            print("Bad luck! , Please try again")

        print("You have only 1 chance left,guess wisely")
        num1 = int(input("Enter your number:"))
        import random
        rand_No = random.randint(1,10)
        print("My number is: ",rand_No)
        if num1==rand_No:
            print("Bravo!, You are more smarter than me ")
        else:
            print("Bad luck! , Please try again")
        break
    
    print("Your chances have exhausted, Please restart the game if you want to play further")


    
