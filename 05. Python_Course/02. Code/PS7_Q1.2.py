# Write a decorator timer that calculates how long a function takes to execute.
# Test it with a function that sums numbers from 1 to 1,000,000.

import time as TM

# Below is Decorator Fucntion Which is start running before actual function and stop running after function so we are measuring time between it.
def timer(func):
    def Wrapper():
       time1 = TM.time()
       func()
       time2 = TM.time()
       Exttime = time2 - time1
       print(Exttime)
    return Wrapper

@timer
def sum_of_Number_With_forloop():
    total = 0
    for n in range(100000001):
        total += n

    return print(total)

@timer
def sum_of_Number_With_Whileloop():
    i = 0
    total = 0
    while i <= 100000000:
        total += i
        i +=1
    return print(total)


sum_of_Number_With_forloop()
sum_of_Number_With_Whileloop()