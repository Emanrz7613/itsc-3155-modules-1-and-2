row_num = int(input('Enter a row num from 1 to 5: '))
col_num = int(input('Enter a col num from 1 to 5: '))
for x in range(1,6):
    if x is row_num:
        for i in range(1,6):
            if i is col_num:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print('')
    else:
        for b in range(0,5):
            print('0', end=' ')
        print('')