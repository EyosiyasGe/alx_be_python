number = int(input("Enter a number to see its multiplication table:"))
for a in range(1,11) :
    result = number * a
    print ( number, "* ", a ," =", result )
    a +=1
