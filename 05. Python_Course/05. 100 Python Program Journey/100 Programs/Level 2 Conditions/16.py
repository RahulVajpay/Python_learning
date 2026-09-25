# 16. Check Voting Eligibility
# Solution ==>

import time as TM
import calendar as Cal
import os

time = int(TM.strftime("%H"))

def Greet():
    if time < 12:
        print("Good Morning!!")
    elif time > 12 and time < 18:
       print("Good Afternnon!!")
    else:
       print("Good Evening !!")
    print("\t\tWelcome to Bharat Vote Regestration Portal.")

def Age_Calculator(DOB):
    _CurrentYear  = int(TM.strftime("%Y"))
    _CurrentMonth = int(TM.strftime("%m"))
    _CurrentDay   = int(TM.strftime("%d"))
    _DOBDay   = int(DOB[0])
    _DOBMonth = int(DOB[1])
    _DOBYear  = int(DOB[2])

    if _DOBYear > _CurrentYear:
        return"You Have Entered Wrong Date of Birth....."
    else:
        if _DOBMonth > 12:
           return"You have Entered a Wrong Date of Birth...."
        else:
            _NumberOfDays = Cal.monthrange(_DOBYear,_DOBMonth)[1]
            if _DOBDay > _NumberOfDays:
                return "You have Entered a Wrong Date of Birth...."
            else:
                if _CurrentDay < _DOBDay and _CurrentMonth < _DOBMonth:
                        _age = _CurrentYear - 1 - _DOBYear
                        return _age
                elif _CurrentDay > _DOBDay and _CurrentMonth > _DOBMonth:
                        _age =  _CurrentYear - _DOBYear
                        return _age
                elif _CurrentDay > _DOBDay and _CurrentMonth < _DOBMonth:
                        _age =  _CurrentYear - 1 - _DOBYear
                        return _age
                elif _CurrentDay == _DOBDay and _CurrentMonth < _DOBMonth:
                        _age =  _CurrentYear - 1 - _DOBYear
                        return _age
                elif _CurrentDay == _DOBDay and _CurrentMonth > _DOBMonth:
                        _age =  _CurrentYear - _DOBYear
                        return _age
                elif _CurrentDay > _DOBDay and _CurrentMonth == _DOBMonth:
                        _age =  _CurrentYear - _DOBYear - 1
                        return _age
                elif _CurrentDay < _DOBDay and _CurrentMonth == _DOBMonth:
                        _age =  _CurrentYear - _DOBYear - 1
                        return _age
                elif _CurrentDay < _DOBDay and _CurrentMonth > _DOBMonth:
                        _age =  _CurrentYear - _DOBYear
                        return _age
                elif _CurrentDay == _DOBDay and _CurrentMonth == _DOBMonth:
                        _age =  _CurrentYear - _DOBYear
                        return _age

Greet()                
while True:
     _DOB = input(f"Please Enter your D.O.B in DD/MM/YYYY Format. : ")
     _DOBLIST = _DOB.split("/")
     try:
          if len( _DOBLIST) ==3 and int(_DOBLIST[0]) > 0 and int(_DOBLIST[1]) > 0 and int(_DOBLIST[2]) > 0:
                break
     except ValueError:
           print("Please Enter a Valid Date of Birth....") 

if isinstance(Age_Calculator(_DOBLIST), int):
      if Age_Calculator(_DOBLIST) >= 18:
            input("You Are Eligible for Voting Let's Start the Forum Filling Process. Press Enter to Start the Process.")
            os.system('cls')
            Greet()
            _fname = input("Please Enter your First Name    : ")
            _lname = input("Please Enter your Last Name     : ")
            while True:
                 _sex   = input("Please Enter your Gender (M/F). : ")
                 try:
                    if _sex.lower() == "m" or _sex.lower() == "f":
                         break
                 except ValueError:
                      print("Please Enter Gender as per Instructed.")
            print("Thanks for Providing Information. Please Find it Below.")
            print("-------------------------------------------------------")
            print(f"First Name : {_fname}\nLast Name  : {_lname}\nGender     : {_sex}\nD.O.B      : {_DOB}\n")
            print("-------------------------------------------------------")      
      else:
           print(f"You Are Not Eligible for Voting Please Try After {_DOBLIST[0]}/{_DOBLIST[1]}/{int(_DOBLIST[2]) + 18} ...")                    
else:
      print(Age_Calculator(_DOBLIST))      

