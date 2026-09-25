import time
print("Welcome to the World of Learning Py Program!")
Name = input("May I know your name? : ")
timeStamp = time.strftime("%H:%M:%S")
if timeStamp < "12:00:00":
    print("Good morning! " + Name)
elif timeStamp < "18:00:00":
    print("Good afternoon! " + Name)
else:    
    print("Good evening! " + Name)
end = input("Press Enter to exit the program.")

