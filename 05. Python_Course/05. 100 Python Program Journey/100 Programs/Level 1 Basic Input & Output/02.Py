# 2. Take name input and greet user
# Solution ==>

import time as TM

f_name = input("Plase Enter your Full Name : ")

hour = int(TM.strftime("%H"))

if hour < 12:
    print(f"Hi Good Morning !! {f_name}.")
elif hour > 12 and hour < 18:
    print(f"Hi Good Afternoon !! {f_name}.")
else:
    print(f"Hi Good Evening !! {f_name}.")

print(f"Good Bye {f_name}!! Have a Good Day Ahead.")