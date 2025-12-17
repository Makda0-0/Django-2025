from abc import ABC, abstractmethod
class transport(ABC):
    @abstractmethod
    def move(self):
        pass
class bus(transport):
    def move(self):
        return "The bus is driving on the road." 
class train (transport):
    def move(self):
        return "The train is running on the tracks."
bus1=bus()
train1=train()  

transports=[bus1,train1]
for transport in transports:
    print(transport.move())