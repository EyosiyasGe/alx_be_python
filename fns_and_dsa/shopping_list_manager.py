# initial shopping list is empty
# while cart is yes 
    # ask the user what they need to do
        # if user selects 1
            # ask what the user wants to add
            # add the input to the list
            # print the list
            # ask the user if they want to add more 
                # if yes 
                    # add the input
                    # print the list
                # elif 
                    # break
                




shoping_list=[]
cart= "yes"
while cart=="yes":
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    x= input("enter number ")
    while x =="1" :
        shoping_list.append(input('Add the Item '))
        print(shoping_list)
        y= input('Do You Need to add another item? Y/N ').upper()
        if y=='y' :
            for i in y:
                a=shoping_list.append(input('Add the Item '))
                print(a)
        elif y == "n" :
            break
        else:
    else :
        break