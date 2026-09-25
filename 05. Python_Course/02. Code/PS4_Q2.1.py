# Write a function full_name(first, last) that takes first name and last nameas parameters and returns a single string in the format "First Last"
# Solution ==>

def FullName(fname, lname, age, sex):
    if sex.lower() == "f":
        return print(f"Hi Mrs. {fname} {lname} Have a Good Day !!. You are {age} years old.".title())
    elif sex.lower() == "m":
        return print(f"Hi Mr. {fname} {lname} Have a Good Day !!. You are {age} years old.".title())

print("Welcome to The Basic Information Collection Program.".title())
_fname = input("Please Enter your first name. : ".title())
_lname = input("Please Enter your Last  name. : ".title())
while True:
    try:
        _age = int(input("Please Enter your age.        : ".title()))
        if _age <=0:
            print("Please Enter a age in positive number".title())
        else:
            break
    except ValueError:
        print('Please Enter a valid Age..'.title())
while True:
    try:
        _sex = input("Please Enter your sex (M\\F)   : ".title())
        if _sex in ("f", "F", "M", "m"):
            break
        else:
            print("Please Enter the sex as depicted above.".title())
    except ValueError:
        print('Please Enter the sex as depicted above.')
FullName(_fname, _lname, _age, _sex)
end = input("Press Enter to Exit The Program.".title())