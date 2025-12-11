class student:
    def __init__(self,grade):
        self.__grade=grade
    def set_grade(self,new_grade):
        self.__grade=new_grade
    def get_grade(self):
        return self.__grade
s1=student(45)
print(s1.get_grade())   
s1.set_grade(85)
print(s1.get_grade())