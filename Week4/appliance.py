from abc import ABC,abstractmethod


class appliance(ABC):
       @abstractmethod
       def turn_0n(self):
           pass#place holder
       
       @abstractmethod
       def turn_off(self):
           pass#place holder
class WashingMachine(appliance):
     def __init__(self,brand):
          self.brand=brand
          self.is_on=False
          super().__init__()
     def turn_0n(self):
         return f"{self.brand} Washing Machine is now ON"
     
     def turn_off(self):
         return f"{self.brand} Washing Machine is now OFF"
wm = WashingMachine("LG")
print(wm.turn_0n())
print(wm.turn_off())      