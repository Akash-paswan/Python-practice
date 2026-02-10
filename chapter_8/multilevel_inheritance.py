#  Multilevel inheritance 
class Car:
    @staticmethod
    def start():
         print("car started --")

    @staticmethod
    def stop():
         print("car stopped--")
         
         
class ToyotaCar(Car):
  def __init__(self,name):
   self.name = name   

class Fortuner(ToyotaCar):
    def __init__ (self,brand):
        self.brand = brand   

car1 = Fortuner("diesel")       
car2 = Fortuner("petrol")


print(car1.stop())
print(car1.start())      # ise hm car1.start() likh skte haiu      