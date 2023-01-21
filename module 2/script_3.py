def return_dict(my_string):
    my_string = my_string.lower()
    my_string = my_string.replace(" ", "")
    count_dict = {}
    for i in my_string:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    return count_dict

my_string = input("Enter a string: ")
print(return_dict(my_string))

