cube_until = int(input('Enter an Integer greater than 1: '))
if cube_until < 1 :
    print('value must be greather than 1')
else :
    for x in range(0,cube_until + 1):
        print('The cube of ' + str(x) + ' is ' + str(x**3))