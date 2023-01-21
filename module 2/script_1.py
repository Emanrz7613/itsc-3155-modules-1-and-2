def get_unique_list(my_list):
    unique_list = []
    for x in range(len(my_list)):
        if unique_list.count(my_list[x]) > 0:
            continue
        else:
            unique_list.append(my_list[x])
    return unique_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
