# store details of a book: title, Author, price, and number of copies calculate total
# inventory value

with open("Library Records.txt","r") as file:
    record=eval(file.read())

print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")
print("------------------------------------")
while True:
    print("Enter 1 to Add a New Book\nEnter 2 to Search a Book\nEnter 3 to update the data of existing book\nEnter 4 to Issue a Book\nEnter 5 to Return a Book\nEnter 6 to show Library Stats")
    print("Enter 0 to exit")

    choice=int(input("Enter your choice: "))

    if choice==0:
        break

    elif choice==1:
        print("YOU CHOSE TO ADD A NEW BOOK TO LIBRARY")
        name=input("Enter Book Name: ").lower()
        if name in record:
            print("Book Already Exists Choose Option 3 to Update Existing details")
        else:
            author=input("Enter the name of the Author: ")
            price=int(input("Enter Book Price: "))
            copies=int(input("Enter Book Copies: "))
            record[name] = {
                "Author": author,
                "Price": price,
                "Copies": copies
            }

            with open("Library Records.txt", "w") as file:
                file.write(str(record))

    elif choice==2:
        print("YOU CHOSE SEARCH LIBRARY")
        search_book=input("Enter Book Name to Search: ").lower()
        if search_book in record:
            print(record[search_book])
        else:
            print("Book Not Found")

    elif choice==3:
        print("YOU CHOSE TO UPDATE THE BOOK DETAILS IN LIBRARY")
        updt_book=input("Enter Book Name to Update: ").lower()
        if updt_book in record:
            author = input("Enter the name of the Author: ")
            price = int(input("Enter Book Price: "))
            copies = int(input("Enter Book Copies: "))
            record[updt_book] = {
                "Author": author,
                "Price": price,
                "Copies": copies
            }

            with open("Library Records.txt", "w") as file:
                file.write(str(record))
        else:
            print("Book Not Found")

    elif choice==4:
        print("YOU CHOSE TO ISSUE A BOOK FROM LIBRARY")
        enter_book=input("Enter Book Name to Issue: ")
        if enter_book in record:
            if record[enter_book]["Copies"] <1 :
                print("All copies issued")
            else:
                print("Book Found")
                name=input("Enter Student Name: ")

                with open("IssuanceLog.txt", "a") as file:
                    file.write(name+" issued "+enter_book+"\n")

                record[enter_book]["Copies"] -= 1
                print (enter_book+" Issued")

                with open("Library Records.txt", "w") as file:
                    file.write(str(record))

        else:
            print("Book Not Found")

    elif choice==5:
        print("YOU CHOSE TO RETURN THE BOOK TO LIBRARY")
        return_book = input("Enter Book Name: ").lower()
        if return_book in record:
            name = input("Enter Student Name: ")
            with open("IssuanceLog.txt", "a") as file:
                file.write(name + " returned " + return_book + "\n")
            record[return_book]["Copies"] += 1

            with open("Library Records.txt", "w") as file:
                file.write(str(record))
        else:
            print("Book Not Found")

    elif choice==6:
        print("LIBRARY STATS")
        print("-------------")
        print(record)
        print("INVENTORY VALUE")
        print("---------------")
        total_value = 0
        for book in record:
            total_value += record[book]["Price"] * record[book]["Copies"]
        print("Total Inventory Value:", total_value, "Rs")

    else:
        print("Invalid Choice")