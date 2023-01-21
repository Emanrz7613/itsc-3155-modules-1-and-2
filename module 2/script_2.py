# referenced https://www.w3schools.com/python/python_dictionaries.asp
def get_combined_dict(my_dict_1, my_dict_2):

    new_dict = {}

    for key, value in my_dict_1.items():
        if (key in my_dict_2.keys()):
            new_dict[key] = value + my_dict_2[key]
    return new_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)


    
