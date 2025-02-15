def calculator():
    print("Simple Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error: Division by zero"
    }
    
    result = operations.get(operation, "Invalid operation")
    print("Result:", result)

calculator()