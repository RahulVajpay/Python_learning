# Q 4.2 Write a program that keeps asking the user to enter a password until they enter the correct one.
# Solution.==>

import os

print("Welcome to Swara Solutions Private Limited!")
f_name = input("Please enter your first name: ")
l_name = input("Please enter your last name: ")
mobile = input("Please enter your mobile number: ")
password = input("Please enter your password: ")
print(f"Thank you {f_name.capitalize()} {l_name.capitalize()} for registering with us. Your mail id is {f_name.lower()}.{l_name.lower()}@swarasolutions.com")

input("Press Enter to go to Login Page...")
os.system('clear')

print("Welcome to Swara Solutions's Login Page!")
while True:
    try:
        mail_id = input("Please enter your mail id: ")
        if mail_id == f"{f_name.lower()}.{l_name.lower()}@swarasolutions.com":
            break
    except ValueError:
        print("Incorrect mail id Please try again.")
while True:
    try:
        passw = input("Please enter your password: ")
        if passw == password:
            print(f"Welcome {f_name} {l_name} to Swara Solutions Private Limited!")
            break
    except ValueError:
            print("Please Enter Correct Passoword.")
end = input("Thanks for Visiting Swara Solutions.Press enter to exit.")
