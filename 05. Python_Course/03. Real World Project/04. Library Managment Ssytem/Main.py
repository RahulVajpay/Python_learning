
import LMS as LMS

Book_Databse = []

LMS.Greet()

while True:
    print('''\nPlease Enter Your Choice Listed Below.
      1. Add Book
      2. Search Book
      3. Issue Book
      4. Return Book
      5. View All Books
      6. Exit\n''')
    try:
        Choice = int(input("Please Enter Your Choice. : "))
        if Choice < 1 or Choice > 6:
            print("Please Enter a Valid Choice.")
        elif Choice == 1:
            LMS.Add_Book(Book_Databse)
        elif Choice == 2:
            LMS.Search_Book(Book_Databse)
        elif Choice == 3:
            LMS.Issue_Book(Book_Databse)
        elif Choice == 4:
            LMS.Return_Book(Book_Databse)
        elif Choice == 5:
            LMS.Display_Books(Book_Databse)
        elif Choice == 6:
            break
    except ValueError:
        print("Please Enter a Valid Choice.")
print("Thanks For Using the Application...")
