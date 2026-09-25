#===== LIBRARY MANAGEMENT SYSTEM =====
#1. Add Book
#2. Search Book
#3. Issue Book
#4. Return Book
#5. View All Books
#6. Exit

# Greet.
def Greet():
    print("=========================================")
    print("||   Welcome to Swara Public Library   ||")
    print("=========================================")

# Add Books.
def Add_Book(BookDatabase):
    Book_ID     = input("Please Enter the Book ID     : ")
    for Book in BookDatabase:
      if Book['Book ID'] == Book_ID:
        print("Book ID Already Exists.")
        return
    Book_Name   = input("Please Enter the Book Name   : ")
    Book_Author = input("Please Enter the Book Author : ")
    Book_Status = "Available"

# Book Set.
    book_Set =  {
                 "Book ID"     : Book_ID, 
                  "Book Name"   : Book_Name,
                  "Book Author"   : Book_Author,
                  "Book Status" : Book_Status
                  }
    
# Add Book Set to Book Database.
    BookDatabase.append(book_Set)
    print("Book Added Successfully.....")

# Search Book.
def Search_Book(BookDatabase):
    if len(BookDatabase) == 0:
        print("No Book Found in Database.")
    else:
        Search_Book_ID = input("Please Enter the Book ID Which you want to Search : ")
        Book_Found = False
        for Books in BookDatabase:
            if Books['Book ID'] == Search_Book_ID:
                Book_Found = True
                print("================================================")
                print("|| Please Find your Book Detail Listed Below. ||")
                print("================================================")
                print(f"Book ID     : {Books['Book ID']}")
                print(f"Book Name   : {Books['Book Name']}")
                print(f"Book Author : {Books['Book Author']}")
                print(f"Book Status : {Books['Book Status']}")
                print("--------------------------------------------------")
                break
        if Book_Found == False:
            print("Book Not Found...")

# Issue Book.
def Issue_Book(BookDatabase):
    if len(BookDatabase) == 0:
        print("No Book Found in Database.")
    else : 
        Book_ID = input("Please Enter Book ID You Want to Book. : ")
        BookFound = False
        for Book in BookDatabase:
            if Book['Book ID'] == Book_ID and Book['Book Status'] == "Available":
                BookFound = True
                Book_Req = input("Your Book is Available for Issue.Press Y For Book or N for Cancel the Booking. : ")
                if Book_Req.lower() == "y":
                    Book['Book Status'] = "Issued"
                    print(f"Congratulations !! Your Book {Book['Book Name']} is Issued to You.Happy Learning Ahead")
                elif Book_Req.lower() == "n":
                    print("Thanks for Using the Library Management System....")
            elif Book['Book ID'] == Book_ID and Book['Book Status'] == "Issued":
                BookFound = True
                print("Book is already issued.")
                break
        if BookFound == False:
                print("Book Not Found...")

# Return Book.    
def Return_Book(BookDatabase):
    if len(BookDatabase) == 0:
        print("No Book Found in Database.")
    else : 
        Book_ID = input("Please Enter Book ID You Want to Return. : ")
        BookFound = False
        for Book in BookDatabase:
            if Book['Book ID'] == Book_ID and Book['Book Status'].lower() == "issued":
                BookFound = True
                Book['Book Status'] = "Available"
                print(f"Thanks For Returning the Book {Book['Book Name']}.")
                break
            elif Book['Book ID'] == Book_ID and Book['Book Status'].lower() == "available":
                BookFound = True
                print("This Book is Never Issued. Please Check With Other Library.")
                break
        if BookFound == False:
            print("Book Not Found...")

# Show All Books.
def Display_Books(BookDatabase):
    if len(BookDatabase) == 0:
        print("No Book Found in Database.")
    else:
        print("Please Find the List of All Books listed Below.")
        for Book in BookDatabase:
            print("----------------------------------------")
            print(f"Book ID     : {Book['Book ID']}")
            print(f"Book Name   : {Book['Book Name']}")
            print(f"Book Author : {Book['Book Author']}")
            print(f"Book Status : {Book['Book Status']}")
        print("All Books List Printed Successfully.....")
