
import time
import os

# Greet Function
def MainPagegreet():
   timeStamp = time.strftime("%H:%M:%S")
   if timeStamp < "12:00:00":
    print(f"{timeStamp}\t\t\t   Good Morning!!")
   elif timeStamp < "18:00:00":
    print(f"{timeStamp}\t\t\t   Good Afternoon!!")
   else:    
    print(f"{timeStamp}\t\t\t   Good Evening!!")
   print("=================================================")
   print("||    Welcome to Swara Solutions Pvt. Ltd.     ||")
   print("=================================================")

# Account_Creation_page
def Account_Creation_page(AccountDatabase):
  print("    Welcome to Swara Solutions Account Creation Page.     ")

  # Taking Require Account Creation information
  first_name = input("Please Enter your first name.                    : ".title())
  last_name  = input("Please Enter your Last name.                     : ".title())
  d_o_b      = input("Please Enter Your Date Of Birth In (DD/MM/YYYY). : ")
  while True:
    _gender    = input("Please Enter your Gender (M\F).                  : ".title())
    if _gender.lower() in ("m" , "f"):
      break
    else:
      print("Please enter Gender as per Instruction".title())
  mobile_no  = input("Please Enter your mobile Number.                 : ".title())
  password   = input("Please Enter your Strong Password.               : ".title())
 
 # To Store Account information of Swara Solution EMS Page.
  AccountDatabase_store = { "Email ID" : (first_name.lower() + "." + last_name.lower() + "@swarasolutions.com"),
                            "Password" : password,
                             "Name"    : (first_name.title() + " " + last_name.title()),
                             "Gender"  : _gender
                             }
  
 # To Add Account information of Swara Solution EMS Page.
  AccountDatabase.append(AccountDatabase_store)

 # Information Print 
  if _gender.lower() =="m":
    print(f"Welcome Mr. {first_name} {last_name} to Swara Solution Pvt. Ltd.")
    print(f"Your Account created Successfully !! Your login id is {first_name.lower()}.{last_name.lower()}@swarasolutions.com")
  else:
    print(f"Welcome Mrs. {first_name} {last_name} to Swara Solution Pvt. Ltd.")
    print(f"Your Account created Successfully !! Your login id is {first_name.lower()}.{last_name.lower()}@swarasolutions.com")
  end = input("Press Enter to Go to Main Menu.".title())
  os.system('cls')
  MainPagegreet()

# Account_Login_page
def Account_Login_page(AccountDatabase):
  os.system('cls')
  MainPagegreet()
  print("Welcome to Swara Solutions Account Login Page.")
  while True:
    emailid = input("Please Enter your Login Email ID: ")
    user_found = False
    for user in AccountDatabase:
     if user["Email ID"] == emailid:
        user_found = True
        while True:
         password = input("Please Enter your Account Password: ")
         if user["Password"] == password:
            print("You have Logged in Successfully....")
            end = input("Press Enter to Go To Swara Solutions Employee Management System.")
            return
         else:
          print("Please Enter a valid password....")
    if user_found == False:
      print("User Information Doesn't Exist. Please enter a valid Email ID")

# EMS Greet Page.
def EMSPagegreet(AccountDatabase):
  os.system('cls')
  timeStamp = time.strftime("%H:%M:%S")
  for user in AccountDatabase: 
    if timeStamp < "12:00:00":
     print(f"{timeStamp}\t  Good Morning!! {user['Name']}")
    elif timeStamp < "18:00:00":
     print(f"{timeStamp}\t  Good Afternoon!! {user['Name']}")
    else:    
     print(f"{timeStamp}\t  Good Evening!! {user['Name']}")
  print("=================================================")
  print("||    Welcome to Emlpoyee Management System    ||")
  print("=================================================")

# Add Employee to Database
def Add_Employee(EmloyeeDatabase):
  Emp_FName = input("Please Enter the Emloyee First Name.            : ")
  Emp_LName = input("Please Enter the Emloyee Last  Name.            : ")
  Emp_DOB   = input("Please Enter the Emloyee D.O.B in (DD/MM/YYYY). : ")
  Emp_DOJ   = input("Please Enter the Emloyee D.O.J in (DD/MM/YYYY). : ")
  Emp_MOB   = input("Please Enter the Emloyee Mobile Number.         : ")
  Emp_Pcard = input("Please Enter Emloyee's Pan Card Detail          : ")
  Emp_Dept  = input("Please Enter Emloyee's Department               : ")
  while True:
    try : 
      Emp_SAL   = input("Please Enter the Emloyee Gross Salary.          : ")
      break
    except ValueError:
      print("Please Enter a Valid Salary Amount.")
  
 # To Store Employee Inforamation in a Dictionary.
  tempEmployee_Data = { "Employee Name" : (Emp_FName + " " +Emp_LName),
                       "Employee DOB"   : Emp_DOB,
                       "Employee DOJ"   : Emp_DOJ,
                       "Employee MOB"   : Emp_MOB,
                       "Employee Dept"  : Emp_Dept,
                       "Employee PCARD" : Emp_Pcard,
                       "Employee SAL"   : Emp_SAL,}
  
  # To Store Employee Inforamation in main Database.
  EmloyeeDatabase.append(tempEmployee_Data)

# View All Employee to Database
def View_Employees(EmloyeeDatabase):
  print("---View All Employee Deatils Listed below---")
  if len(EmloyeeDatabase) == 0:
    print("No Employee Information Found in the Database..")
  for employees in EmloyeeDatabase:
    print("------------------------------------------------------")
    print(f"Employee Name         : {employees['Employee Name']} ")
    print(f"Employee D.O.B        : {employees['Employee DOB']}  ")
    print(f"Employee D.O.J        : {employees['Employee DOJ']}  ")
    print(f"Employee Mobile No.   : {employees['Employee MOB']}  ")
    print(f"Employee Department   : {employees['Employee Dept']} ")
    print(f"Employee Pan Card     : {employees['Employee PCARD']}")
    print(f"Employee Gross Salary : {employees['Employee SAL']}  ")
  print("All Employee Details in the Database Printed Successfully.....") 

# Search Employee by Pan Card.
def Search_Employee(EmloyeeDatabase):
  if len(EmloyeeDatabase) == 0:
    print("No Employee Information Found in the Database..")
  else:
    _pcard = input("Please Enter the Emlployee Pan Card No. : ")
    Emp_found = False
    for employees in EmloyeeDatabase:
      if employees['Employee PCARD'] == _pcard.upper():
       Emp_found = True
       print("-------Employee Found-------------")
       print(f"Employee Name         : {employees['Employee Name']} ")
       print(f"Employee D.O.B        : {employees['Employee DOB']}  ")
       print(f"Employee D.O.J        : {employees['Employee DOJ']}  ")
       print(f"Employee Mobile No.   : {employees['Employee MOB']}  ")
       print(f"Employee Department   : {employees['Employee Dept']} ")
       print(f"Employee Pan Card     : {employees['Employee PCARD']}")
       print(f"Employee Gross Salary : {employees['Employee SAL']}  ")
    if Emp_found == False:
      print("User Information Doesn't Exist. Please enter a valid Pan Card Detail.")   

# Remove Employee Data.
def Remove_Employee (EmloyeeDatabase):
  if len(EmloyeeDatabase) == 0:
    print("No Employee Information Found in the Database..")
  else:
    _pcard = input("Please Enter the Emlployee Pan Card No. : ")
    Emp_found = False
    for employees in EmloyeeDatabase:
      if employees['Employee PCARD'] == _pcard.upper():
       Emp_found = True
       EmloyeeDatabase.remove(employees)
       print("Employee Deleted Successfully.....")
    if Emp_found == False:
      print("User Information Doesn't Exist. Please enter a valid Pan Card Detail.") 

# Show Show Unique Departments List.
def Show_Unique_Departments(EmloyeeDatabase):
  uniqe_dpartment_set = set()
  uniqe_dpartment_list = []
  if len(EmloyeeDatabase) == 0:
    print("No Employee Information Found in the Database..")
  else :
    for employees in EmloyeeDatabase:
      uniqe_dpartment_set.add(employees['Employee Dept'])
    for department in uniqe_dpartment_set:
     uniqe_dpartment_list.append(department)
    i = 0
    print("List of All Department listed Below.")
    while i < len(uniqe_dpartment_list):
      print(f"{i+1}. {uniqe_dpartment_list[i]}")
      i +=1
  print("All Available Department in Database Printed Successfully.")

# Calculate Average salary of All Employee in Database.
def Calculate_Average_Salary(EmloyeeDatabase):
 employee_Salary = []
 if len(EmloyeeDatabase) == 0:
    print("No Employee Information Found in the Database..")
 else :
    for employees in EmloyeeDatabase:
      employee_Salary.append(employees['Employee SAL'])
    i = 0
    Total_salary = 0
    Count = 0
    while i < len(employee_Salary):
      Total_salary += float(employee_Salary[i])
      i +=1
      Count +=1
    print(f"The Total Average Salary of All {Count} Employees in Swara Solutions is Rs. {Total_salary/Count}.")

