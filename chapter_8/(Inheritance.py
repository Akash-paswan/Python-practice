class Car:
    color = "Black"
    @staticmethod
    def start():
         print("car started --")

    @staticmethod
    def stop():
         print("car stopped--")
         
         
class ToyotaCar(Car):
  def __init__(self,name):
   self.name = name   

  

car1 = ToyotaCar("fortuner")       
car2 = ToyotaCar("Scorpio")


print(car1.name)
print(car1.start())
print(car2.stop())
print(car2.color)


# Car.stop()
# Car/start()   # aise bhiu hm kar skte the 
    
