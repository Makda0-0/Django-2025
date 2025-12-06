def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation=input("Enter operation (+, -, *, /): ")
if operation=='+':
     result = add(num1, num2)
elif operation=='-' :
       result = subtract(num1, num2) 
elif operation=='*' :
       result = multiply(num1, num2) 
elif operation=='/' :
       result = divide(num1, num2) 
else:
        result = "Invalid operation"
    
    
print("Result:", result)
                       