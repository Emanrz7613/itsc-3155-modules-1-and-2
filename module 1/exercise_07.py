list = []
while True:
    num = input('Enter a number or QUIT to quit: ')
    if num == 'QUIT':
        break
    else:
        num = int(num)
        list.append(num)
print('All Nums: ' + str(list))
even_list = []
for i in range(len(list)):
    if list[i] % 2 == 0:
        even_list.append(list[i])
print('Even Nums: ' + str(even_list))

#referenced https://blog.finxter.com/how-to-get-specific-elements-from-a-list/