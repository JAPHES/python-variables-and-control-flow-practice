#a simple calculator

# Function to perform basic arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error Division by zero is not allowed."
    else:
        return "invalid operator"

    #user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator =input("Enter an operator (+, -, *, /): ")

#calculate and display results
result = calculate(num1, num2, operator)
print(f"The result is {result}")

