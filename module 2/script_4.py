i = 1
sum = 0
while i <= 5:
    try:
        x = int(input("Enter int #" + str(i) + ": "))
        sum += x
        i += 1        

    except ValueError:
        print("Invalid input. Please enter an int.")  
    
    
    
print("Your sum is ",sum)