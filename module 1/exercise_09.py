list = []
for i in range(5):
    list.append(input('Enter a word: '))
print('Words: ' + str(list))
print('One String: ', end='')
print (*list)
