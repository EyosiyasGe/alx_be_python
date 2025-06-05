from arithmetic_operations import perform_operation
def main():
    print("Arithmetic Operations")
    num1=float(input('enter the first number '))
    num2= float(input('enter the first number '))
    operation = input('insert the operation to be performed (add, subtract, multiply, divide): ').strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
if __name__ == "__main__":
    main()
