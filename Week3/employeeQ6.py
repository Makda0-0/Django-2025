class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
       return self.salary*12
    
p1=employee("joe",2000) 
print(f"Annual salary is: {p1.annual_salary()}")   

