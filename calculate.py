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
num1 = 10   
num2 = 5
operator = input("Enter an operator (+, -, *, /): ")
result = calculate(num1, num2, operator)
print(f"The result of {num1} {operator} {num2} is: {result}")

