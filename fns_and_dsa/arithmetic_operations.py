def perform_operation(num1, num2, operation):
    if operation == 'add' :
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'division'  :
        if num2 == 0:
            return print("0 division is impossible") 
        else :
            return num1/num2
    else :
        return print(" please chose proper operation")
