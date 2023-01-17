num_grade = input('Enter a grade from 0 to 100: ')
num_grade = int(num_grade)
if num_grade < 60: 
    print('Your grade is an F')
elif num_grade < 70:
    print('Your grade is a D')
elif num_grade < 80:
    print('Your grade is a C')
elif num_grade < 90:
    print('Your grade is a B')
else: 
    print('Your grade is an A')