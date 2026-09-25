import time
timestamp = time.strftime("%H:%M:%S")
name = input("What is your name: ")
if timestamp < "12:00:00":
    print(f"Good morning, {name}!")
elif timestamp < "18:00:00":
    print(f"Good afternoon, {name}!")
else:
    print(f"Good evening, {name}!")
end = input("Press Enter to exit.")