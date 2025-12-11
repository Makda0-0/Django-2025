def get_grade(student_grades,student_name):
 try:    
     with open("students.txt","r") as file:
        content=file.read()
     with  open("students.txt","r") as file:
        for line in file:
            print (line.strip())
 except FileNotFoundError:
   print("File missing!")              
 except ValueError:
    print("Student not found in the system")
student=int(input("Enter student name:"))
get_grade(student)
