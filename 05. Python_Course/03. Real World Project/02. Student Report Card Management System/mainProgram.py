
import Student_Report_Card_Management_System as SRCMS

students = []

SRCMS.greet()
while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Show Class Topper")
    print("6. Exit")
    try : 
        choice = int(input("\nEnter Your Choice : "))
        if choice > 6 or choice<=0:
            print("Please Enter a Valid Choice...\n")
        elif choice == 1 :
            SRCMS.Add_Student(students)
        elif choice == 2 :
            SRCMS.Display_Students(students)
        elif choice == 3 :
            SRCMS.Search_Student(students)
        elif choice == 4 :
            SRCMS.Delete_Student(students)
        elif choice == 5 :
            SRCMS.Topper_Student(students)
        elif choice == 6 :
            print("Thanks for Using the Application...")
            break
    except ValueError:
        print("Please Enter a Valid Choice...\n")

    



