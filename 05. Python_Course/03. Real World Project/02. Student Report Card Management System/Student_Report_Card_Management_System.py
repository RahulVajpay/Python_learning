
# Greet Function.
def greet():
    print("===============================================================")
    print("||      WELCOME TO STUDENT REPORT CARD MANAGEMENT SYSTEM     ||")
    print("===============================================================")
    return

# Function to Add Student.
def Add_Student(Student_Datbase):
    Student_name        =       input("Please Enter Student Name                             : ")
    Student_Roll_Number =       input("Please Enter Student Roll Number                      : ")
    Student_Class       =       input("Please Enter Student Class                            : ")
    while True:
        try:
            Englis_Marks        = float(input("Please Enter Student marks Obtained in English        : "))
            if Englis_Marks > 100:
                print("Obtained marks cannot be Graeter than 100")
                continue
            else : 
                break
        except ValueError:
              print("Please Enter a Valid Marks.")
    while True:
        try:
            Hindi_Marks        = float(input("Please Enter Student marks Obtained in Hindi          : "))
            if Hindi_Marks > 100:
                print("Obtained marks cannot be Graeter than 100")
                continue
            else : 
                break
        except ValueError:
            print("Please Enter a Valid Marks.")
    while True:
        try:
            Math_Marks          = float(input("Please Enter Student marks Obtained in Math           : "))
            if Math_Marks > 100:
                print("Obtained marks cannot be Graeter than 100")
                continue
            else : 
                break
        except ValueError:
            print("Please Enter a Valid Marks.")
    while True:
        try:
            Science_Marks       = float(input("Please Enter Student marks Obtained in Science        : "))
            if Science_Marks > 100:
                print("Obtained marks cannot be Graeter than 100")
                continue
            else : 
                break
        except ValueError:
            print("Please Enter a Valid Marks.")       
    while True:
        try:
            S_Science_Marks     = float(input("Please Enter Student marks Obtained in Social Science : "))
            if S_Science_Marks > 100:
                print("Obtained marks cannot be Graeter than 100")
                continue
            else : 
                break
        except ValueError:
            print("Please Enter a Valid Marks.")

# Total Obtained Marks
    Total_Obtained_Marks =Englis_Marks + Hindi_Marks + Math_Marks + Science_Marks + S_Science_Marks   

# Calculate the Todtal Percentage.
    percentage = (Englis_Marks + Hindi_Marks + Math_Marks + Science_Marks + S_Science_Marks)/5

# Grade Logic.
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

#  Store Student Data.
    student_data = {
        "Student Name" : Student_name,
        "Roll Number" : Student_Roll_Number,
        "Class" : Student_Class,
        "English Marks" : Englis_Marks,
        "Hindi Marks" : Hindi_Marks,
        "Math Marks" : Math_Marks,
        "Science Marks" : Science_Marks,
        "S.Science Marks" : S_Science_Marks,
        "Total Obtained Marks" : Total_Obtained_Marks,
        "Percnetage Obtained" : percentage,
        "Grade Obtained" : grade
    }

# Add Student Data.
    Student_Datbase.append( student_data)

    print("\nStudent Added Successfully!\n")

#  Function to display All Student.
def Display_Students(Student_Datbase):
    print("\n========== STUDENT REPORTS ==========")
    if len(Student_Datbase) == 0:
        print("No Student Records Found.\n")
        return
    for student in Student_Datbase:

        print("\n--------------------------------")
        print(f"Name               : {student['Student Name']}")
        print(f"Roll No            : {student['Roll Number']}")
        print(f"Class              : {student['Class']}")
        print(f"English            : {student['English Marks']}")
        print(f"Hindi              : {student['Hindi Marks']}")
        print(f"Math               : {student['Math Marks']}")
        print(f"Science Marks      : {student['Science Marks']}")
        print(f"S.Science          : {student['S.Science Marks']}")
        print(f"Total              : {student['Total Obtained Marks']}")
        print(f"Percentage         : {student['Percnetage Obtained']:.2f}%")
        print(f"Grade              : {student['Grade Obtained']}")
        print("--------------------------------")

# Function to Search Student.
def Search_Student(Student_Datbase):
    print("\n========== SEARCH STUDENT ==========")
    Srch_Roll = input("Please Enter the Roll Number of Student : ")

    for student in Student_Datbase:
        if student["Roll Number"] == Srch_Roll:
            print("\nStudent Found")
            print(f"Name               : {student['Student Name']}")
            print(f"Roll No            : {student['Roll Number']}")
            print(f"Class              : {student['Class']}")
            print(f"English            : {student['English Marks']}")
            print(f"Hindi              : {student['Hindi Marks']}")
            print(f"Math               : {student['Math Marks']}")
            print(f"Science Marks      : {student['Science Marks']}")
            print(f"S.Science          : {student['S.Science Marks']}")
            print(f"Total              : {student['Total Obtained Marks']}")
            print(f"Percentage         : {student['Percnetage Obtained']:.2f}%")
            print(f"Grade              : {student['Grade Obtained']}")
            print("--------------------------------")
        else:
            print("\n Student Not Found....")

# Function to Delete Student.
def Delete_Student(Student_Datbase):
    print("\n========== DELETE STUDENT ==========\n")

    Srch_Roll = input("Please Enter the Roll Number of Student : ")

    for student in Student_Datbase:
        if student["Roll Number"] == Srch_Roll:
            Student_Datbase.remove(student)
            print("Student Deleted Successfully.....")
        else:
            print("\n Student Not Found....")

# Function to Show Student.
def Topper_Student(Student_Datbase):
    print("\n========== SHOW TOPPER ==========\n")

    topper = Student_Datbase[0]

    for student in Student_Datbase:
        if student['Percnetage Obtained'] > topper['Percnetage Obtained']:
            topper = student
    print(f"{topper['Student Name']} is Topper of Class {topper['Class']} and He Obtained {topper['Percnetage Obtained']}% marks.")

