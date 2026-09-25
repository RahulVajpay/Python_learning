# Employee Management System
# Features
# ✅ Add Employee
# ✅ View Employees
# ✅ Search Employee
# ✅ Remove Employee
# ✅ Show Unique Departments (Set)
# ✅ Calculate Average Salary
# ✅ Uses List, Dict, Set, Functions, Loops, Match-Case

import EMS

Account_Database  = []
Employee_Database = []

EMS.MainPagegreet()

while True : 
    print("\n1. Account Creation Page.")
    print("2. Account Login Page.")
    print("3. Exit")
    try : 
        main_choice = int(input("\nEnter Your Choice : "))
        if main_choice > 3 or main_choice<=0:
            print("Please Enter a Valid Choice...\n")
        elif main_choice == 1:
            EMS.Account_Creation_page(Account_Database)
        elif main_choice == 2:
            EMS.Account_Login_page(Account_Database)
            EMS.EMSPagegreet(Account_Database)
            while True:
                print("\n1. Add Employee.")
                print("2. View Employees.")
                print("3. Search Employee.")
                print("4. Remove Employee.")
                print("5. Show Unique Departments.")
                print("6. Calculate Average Salary.")
                print("7. Logout.")
                try : 
                    choice = int(input("\nEnter Your Choice : "))
                    if choice > 7 or choice <= 0:
                        print("Please Enter a Valid Choice...\n")
                    elif choice == 1:
                        EMS.Add_Employee(Employee_Database)
                        print("\nEmployee Data Added Successfully...\n")
                    elif choice == 2:
                        EMS.View_Employees(Employee_Database)
                    elif choice == 3:
                        EMS.Search_Employee(Employee_Database)
                    elif choice == 4:
                        EMS.Remove_Employee(Employee_Database)
                    elif choice == 5:
                        EMS.Show_Unique_Departments(Employee_Database)
                    elif choice == 6:
                        EMS.Calculate_Average_Salary(Employee_Database)
                    elif choice == 7:
                        print("You have Logged out Successfully...")
                        EMS.MainPagegreet()
                        break
                except ValueError:
                    print("Please Enter a Valid Choice...\n")
        elif main_choice == 3:
            break
    except ValueError:
        print("Please Enter a Valid Choice...\n")
print("Thanks for Using Aplication..")

