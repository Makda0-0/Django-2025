from abc import ABC


class employee(ABC):
    

     def calculate_salary(self):
          pass#place holder
          
          
class FullTimeEmployee(employee):
     def __init__(self,salary,):
          self.salary=salary
     def calculate_salary(self):
         return self.salary

     
emp1 = FullTimeEmployee(5000)   
print(f"Full Time Employee Salary: ${emp1.calculate_salary()}")

               