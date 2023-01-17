l1 = []
l2 = []
for x in range(5):
    l1.append(int(input('Enter a number for the first list: ')))
for x in range(5):
    l2.append(int(input('Enter a number for the second list: ')))
print('First List: ' + str(l1))
print('Second List: ' + str(l2))
def common_member(l1, l2):
    result = [i for i in l1 if i in l2]
    return result

print('Common List: ' + str(common_member(l1, l2)))

# referenced geeksforgeeks.org