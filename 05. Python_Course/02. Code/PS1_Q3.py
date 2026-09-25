print('Welcome to the Python course!')
name = input('Please enter your name.         : ')
age =  int(input('Please enter your age.          : '))
height = float(input('Please enter your height in cm. : '))
is_student = input('Are you a student? (Yes/No)    : ')
sex = input('Please enter your sex (M/F).    : ')

if (sex == 'M' or sex == 'm') and (is_student == 'yes' or is_student == 'Yes' or is_student == 'YES'):
    is_student = True
    print('Hello Mr. ' + name + ' !')
    print('your are ' + str(age) + ' years old, ' + str(height) + ' cm tall, and it is ' + str(is_student) + ' that you are a student.')

elif (sex == 'M' or sex == 'm') and (is_student == 'no' or is_student == 'No' or is_student == 'NO'):
    is_student = False
    print('Hello Mr. ' + name + ' !')
    print('your are ' + str(age) + ' years old, ' + str(height) + ' cm tall, and it is ' + str(is_student) + ' that you are a student.')

elif (sex == 'F' or sex == 'f') and (is_student == 'yes' or is_student == 'Yes' or is_student == 'YES'):
    is_student = True
    print('Hello Ms. ' + name + ' !')
    print('your are ' + str(age) + ' years old, ' + str(height) + ' cm tall, and it is ' + str(is_student) + ' that you are a student.')

elif (sex == 'F' or sex == 'f') and (is_student == 'no' or is_student == 'No' or is_student == 'NO'):
    is_student = False
    print('Hello Ms. ' + name + ' !')
    print('your are ' + str(age) + ' years old, ' + str(height) + ' cm tall, and it is ' + str(is_student) + ' that you are a student.')  
print('Thank you for providing your information, ' + name + ' !')
end = input('Press Enter to exit the program. ')