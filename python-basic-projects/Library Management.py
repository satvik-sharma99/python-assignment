# Name : SATVIK SHARMA
# Trainer : Miss Ayushi Jain
# Course : Data Analytics
# Institute : Ws Cube Tech , Jaipur(Raj)

print("Welcome to oxford library")
username = "SATVIK"
password = "data99"
borrowed_books = {}
while True: 
    user = input("enter username: ")
    if user == username:


        ps = input("password: ")
        if ps == password:
            print("login successful")
        else:
            print("password incorrect")
            break

    else:
        print("username incorrect ")
        break

    print("Instructions for the library are as follows:") 
    while True:
        print("""
          press 1 to insert
          press 2 to display list of books 
          press 3 to borrow books
          press 4 to return books
          press 5 to  display borrow books along with name:""")

        choice = int(input("enter your choice between 1-5: "))

        if choice == 1:
            books = {"R D Sharma":5,"HC Verma":5,"Exam Idea":5,"Three men in a boat":5,"Two States":5}
            print("enter the  name of the book you want to add in the library: ")
            add_book = input("enter the book name you want to add: ")
            add_quantity = int(input("enter how many books do you want to add: "))
            books[add_book]=add_quantity
            print(books)


        elif choice == 2:
            for s in books:
                print("Books available currently are:",s)

        elif choice == 3:
            while True:
                user_name=input("enter your name")
                print(books)
                book = input("enter a book name: ")
                if book == books:
                    print("book is  available: ")
                else:
                    break
                quantity = int(input("enter  number of book you want: "))
                books[book] = books[book]-quantity
                borrowed_books[user_name]=book
                choice = input("do you want more book: ")
                if quantity>=3:
                    print("not allowed at a time")
                    break   

                

        elif choice == 4:
            return_book = input(" which book you want to return: ")
            books[return_book] = books[return_book]+quantity
            print("Thanks for returning the book on time: ")

        elif choice == 5:
             print(book)   

        repeat = input("do you want to perform another task? ")
        if repeat == "no": 
            print("Thank you for visting library!, have a nice day")
            break