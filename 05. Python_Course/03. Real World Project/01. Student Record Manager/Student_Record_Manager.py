# Program Goal
# The program should:
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Delete Student
# 5. Exit Program

# Greeting Message.
def Greet():
    print("=========================================================")
    print("||           Welcome to Swara Public School            ||".title())
    print("=========================================================")

# Add Student
def Add_Student(StudentDatabase):
   _StudentFirstName  = input("Please Enter the Student Fisrt Name  : ".title())
   _StudentMidlleName = input("Please Enter the Student Middle Name : ".title())
   _StudentLastName   = input("Please Enter the Student Last Name   : ".title())
   while True:
        _studentGender = input("Please Enter the Gender of Student(M\F) : ".title())
        if _studentGender.lower() in ("m" ,"f"):
            break
        else:
            print("Please Enter the Gender as per the requirment.")
   _studentDOB = input("Please Enter Student Date of Birth in (DD/MM/YYYY) Format : ".title())
   _Studentclass = input("Please enter the Class in Which Student Want to Enroll. : ".title())
   _StudentRoll  = input("Please enter the Register Roll Number of Student .      : ".title())
   _stuFatherName = input("Please Enter the Student Father Name. : ".title())

# Store Student Data
   student_Data = {
        "Student Name"        : (_StudentFirstName + " " + _StudentMidlleName + " " + _StudentLastName  ),
        "Student Gender"      : _studentGender,
        "Student Class"       : _Studentclass,
        "Student Father Name" : _stuFatherName,
        "Student Roll Number" : _StudentRoll
    }
# Add Data to Studenbt Database.
   StudentDatabase.append(student_Data)

   print("\nStudent Added Successfully!\n")

# display Student      
def Display_Student(StudentDatabase):
    if len(StudentDatabase) == 0:
        print("No Student Recored Found in the database.")
    else :
          print("------  Student Records--------")
          print("-------------------------------")
          for student in StudentDatabase:
              print("-------------------------------")
              print(f"Name        : {student['Student Name']}".title())
              print(f"Gender      : {student['Student Gender']}".title())
              print(f"Class       : {student['Student Class']}".title())
              print(f"Father Name : {student['Student Father Name']}".title())
              print(f"Roll Number : {student['Student Roll Number']}".title())
              print("-------------------------------\n")         

# Search Student
def Search_Student(StudentDatabase):
   if len(StudentDatabase) == 0:
     print("No Student Recored Found in the database.")
   else :
       studentRoll = input("Please Enter the Roll Number of Student you want to Serach.")
       for student in StudentDatabase:
           if student['Student Roll Number'] == studentRoll:
               print("---------Student Found ----------")
               print(f"Name        : {student['Student Name']}".title())
               print(f"Gender      : {student['Student Gender']}".title())
               print(f"Class       : {student['Student Class']}".title())
               print(f"Father Name : {student['Student Father Name']}".title())
               print(f"Roll Number : {student['Student Roll Number']}".title())
               print("-------------------------------\n") 

# Student Delete
def Delete_Student(StudentDatabase):
   if len(StudentDatabase) == 0:
     print("No Student Recored Found in the database.")
   else :
       studentRoll = input("Please Enter the Roll Number of Student you want to Delete From Records.")
       for student in StudentDatabase:
           if student['Student Roll Number'] == studentRoll:
               print("---------Student Found ----------")
               print(f"Name        : {student['Student Name']}".title())
               print(f"Gender      : {student['Student Gender']}".title())
               print(f"Class       : {student['Student Class']}".title())
               print(f"Father Name : {student['Student Father Name']}".title())
               print(f"Roll Number : {student['Student Roll Number']}".title())
               StudentDatabase.remove(student)
               print("---Student Deleted Successfully---\n") 