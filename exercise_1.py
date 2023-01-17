string = input('Enter a string: ')
strLength = len(string)
lower = ""
upper = ""
list = [i for i in string]
for i in range(len(list)):
    if (list[i] == " "):
        continue
    else:
        if (list[i] >= 'A' and list[i] <= 'Z'):
            upper += list[i]
        else:
            lower += list[i]

print(lower + upper)
