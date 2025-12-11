class car:
    def __init__(self,make):
        self.make=make
    def get_make(self):
        return f"Make:{self.make}"
c1=car("Mercedes")
print(c1.get_make())
