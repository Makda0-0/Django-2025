
grades = {"John": "A", "Sara": "B", "Musa": "A"}

# the swapped result
swapped = {}


for student, grade in grades.items():
    # If grade already exists as a key in swapped dictionary
    if grade in swapped:
        # Add student to the existing list
        swapped[grade].append(student)
    else:
        # Create new list with this student
        swapped[grade] = [student]


print(swapped)