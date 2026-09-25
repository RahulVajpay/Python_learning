print("\t\t Welcome to Window ChatGpt \t\t")
print("\t\t A Powerful AI Language Model \t\t")
print("\t\t Please Login to Continue \t\t")
username = input("Enter your username: ")
password = input("Enter your password: ")
end = input("\n\t\t Press Enter to Login \t\t")
clear = "\n" * 100
print(clear)
username1 = input("Enter your username: ")
if username1 == username:
    password1 = input("Enter your password: ")
    if password1 == password:
        print("\n\t\t Login Successful! Welcome to Window ChatGpt \t\t")
        print("\t\t Thank You For Using Window ChatGpt! \t\t")
        end = input("Press Enter to exit the program.")
    else:
        print("\n\t\t Incorrect Password!, Your Account is Locked. \t\t")
        print("\t\t Sorry, but you are not authorized to access this system. \t\t")
        end = input("Press Enter to exit the program.")
else:
    print("\t\t Incorrect Username!. Please Try Again. \t\t")
    print("\t\t Sorry, but you are not authorized to access this system. \t\t")
    end = input("Press Enter to exit the program.")

