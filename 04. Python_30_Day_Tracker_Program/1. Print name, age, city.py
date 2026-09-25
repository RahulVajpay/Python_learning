print('\t\t"Welcome to Simple Entry Program !!"')
name = input('Please enter your name: ')
try:
    age = int((input('Please enter your age: ')))
except ValueError:
    print("Invalid input. Please enter a valid age.")
    age = 0                                 # set a default age or handle it as needed
city = input('Please enter your city: ')
try:
    salary = float(input('Please enter your Annual Package: '))
except ValueError:
    print("Invalid input. Please enter a valid salary.")
    salary = 0.0                            # set a default salary or handle it as needed   
print(f"Your name is {name}, you are {age} years Old and Residing in {city} and your Annual Package is Rs.{salary}.") 
end = input('Press Enter to exit...') 