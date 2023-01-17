list = []
for i in range(10): 
    num = int(input('Enter number ' + str(i + 1) +':'))
    list.append(num)
print('Original List: ' + str(list))
res = [i for i in list if list.count(i)==1]
print('Nums that appear once: ' + str(res))