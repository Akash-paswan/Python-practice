class Car:
    def __init__(self,type):
        self.type = type
        
        
    @staticmethod
    def start():
         print("car started --")

    @staticmethod
    def stop():
         print("car stopped--")
         
         

class ToyotaCar(Car):
    def __init__ (self,name, type):
        super().__init__(type)            # (we use super method to call parent classs )jab hmmc child class me se hi hm parent class ko call kar skte hai 
        self.name = name 
        super().start()



car1 = ToyotaCar("prius","electrric")
print(car1.type)
    