# 12. Positive, Negative or Zero
# Solution ==>

print("Hi Welcome to Positive, Negative and Zero Check Program..")
while True:
    try:
        num = float(input("Please Enter a Your Number. "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

if num > 0:
    print(f"{num} is a Postive Number.")
elif num < 0:
    print(f"{num} is a Negative Number.")
else:
    print("You have Entered a Zero.")         