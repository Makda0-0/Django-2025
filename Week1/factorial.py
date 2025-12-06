def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers or non-integers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = int(input("Enter the first number: "))
result = factorial(num)
print(f"Factorial is {result}")
