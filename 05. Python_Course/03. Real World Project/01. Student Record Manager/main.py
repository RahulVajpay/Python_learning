import Student_Record_Manager as SRM

students  = []

SRM.Greet()
while True : 
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    try : 
        choice = int(input("\nEnter Your Choice : "))
        if choice > 5 or choice<=0:
            print("Please Enter a Valid Choice...\n")
        elif choice == 1:
            SRM.Add_Student(students)
        elif choice == 2:
            SRM.Display_Student(students)
        elif choice == 3:
            SRM.Search_Student(students)
        elif choice == 4:
            SRM.Delete_Student(students)
        elif choice == 5:
            break
    except ValueError:
        print("Please Enter a Valid Choice...\n")
print("Thanks for Using Aplication..")



