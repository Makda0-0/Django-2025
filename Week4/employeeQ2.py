from abc import ABC,abstractmethod

class employee(ABC):
       @abstractmethod
       def calculate_salary(self):
           pass#place holder

      
class partTimeEmployee(employee):
     def __init__(self,hourly_rate,hours_worked):
          self.hourly_rate=hourly_rate
          self.hours_worked=hours_worked
     def calculate_salary(self):
         return self.hourly_rate * self.hours_worked
 
 
pt_emp=partTimeEmployee(30,90)
print(f"Part Time Employee Salary: ${pt_emp.calculate_salary()}")