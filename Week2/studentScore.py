def lookup_student_score():
    
    scores = {"John": 85, "Sara": 92, "Fraol": 78}
    
    
    student_name = input("Enter student name: ")
    
    try:
        score = scores[student_name]
        print(f"{student_name}'s score: {score}")
    except KeyError:
        print("Student not found!")


lookup_student_score()