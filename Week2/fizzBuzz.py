
def main():
    n = int(input("Enter a number: "))
    result = fizzBuzz(n)
    
    print(f"\nFizzBuzz results for 1 to {n}:")
    print("-" * 25)
    for i, value in enumerate(result, 1):
        print(f"{i:3}: {value}")

def fizzBuzz(n):
    answer = []
    for i in range(1, n + 1):
        if i % 15 == 0: 
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

if __name__ == "__main__":
    main()