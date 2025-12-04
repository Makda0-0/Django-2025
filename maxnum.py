def find_maximum(numbers):
    if not numbers:
        return "The list is empty."
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

user_input = input("Enter a list of numbers separated by spaces: ")
try:
    user_list = [int(x) for x in user_input.split()]
    result = find_maximum(user_list)
    print(f"The maximum number in the list is: {result}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
