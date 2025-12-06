from datetime import datetime
current_year = datetime.now().year

age=int(input("Enter your age:"))
birth_year = current_year - age

print(f"Your birth year is {birth_year}.")