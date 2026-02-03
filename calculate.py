#Create a calculator which takes two number and an operator and performs the calculation.
#  The calculator should support addition, subtraction, multiplication, and division.
#print the result based on the operator provided.
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
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"    
# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = calculate(num1, num2, operator)
print(f"The result of {num1} {operator} {num2} is: {result}")

operation = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
if operation == 1:
    operator = '+'
elif operation == 2:
    operator = '-'
elif operation == 3:        
    operator = '*'
elif operation == 4:
    operator = '/'
else:
    print("Invalid operation selected.")
    operator = None
if operator:
    result = calculate(num1, num2, operator)
    print(f"The result of {num1} {operator} {num2} is: {result}")
    