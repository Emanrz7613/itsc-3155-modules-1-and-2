from statistics import mean

list_size = int(input('Enter a number: '))
list = []
for x in range(0,list_size):
    list.append(float(input('Enter number ' + str(x + 1) + ': ')))
print('List: ' + str(list))
print('Average: ' + str(mean(list)))