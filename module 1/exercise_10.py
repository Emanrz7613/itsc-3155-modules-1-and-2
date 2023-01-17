string = input('Enter a string: ')
list = [i for i in string]
split = [list[x:x+3] for x in range(0, len(list), 3)]
split_list = []
split_list.append(split)
print(*split_list)


# referenced https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
# referenced https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists