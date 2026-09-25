# Q 1.2 Create a program that checks if a person is eligible to vote (age >= 18)
# Solution ==>

print("Welcome to Bharat Vote Portal.")
while True:
    try:
        age = int(input("Plese Enter Your Currente Age. : "))
        if age <= 0:
            print("Age Should be Greater than Zero.")
        elif age > 0:
            break
    except ValueError:
        print("Please Enter a Valid Number...")
if age >= 18:
    print(f"Hi you are {age} years old you can Vote.")
elif age < 18:
    if 18-age == 1:
        print(f"Hi dear just wait for {18-age} year more after that you are eligible for Vote.")
    elif 18-age > 1:
        print(f"Hi dear just wait for {18-age} years more after that you are eligible for Vote.") 
print("Thanks for using Bharat Vote Portal")
end = input("Press Enter to Exit the Program...")
