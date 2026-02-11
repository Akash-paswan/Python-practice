# class Complex :
#     def __init__(self,real,img):
#      self.real = real
#      self.img = img 
    
#     def showNumber(self):
#        print(self.real,"i +",self.img,"j+") 
    
# # def __add__(self,num2):
# #     newReal = self.real+num2.real
# #     newImg = self.img+ num2.img 
# #     return complex(newReal,newImg)





# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()
              
              
              
# class Complex :
#     def __init__(self,real,img):
#      self.real = real
#      self.img = img 
    
#     def showNumber(self):
#        print(self.real,"i +",self.img,"j+") 
    
#     def  add(self,num2):
#        newReal = self.real+num2.real
#        newImg = self.img + num2.img 
#        return complex(newReal,newImg)



# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1.add(num2)
# print(num3)                           # num3.showNumber()

# agar hme  47,48 wala line nhi likhna hai to meas object se call nhi karna hai to 
# hme direct    print(num1num2) karna hai to dunder fun kamuse karna higa 

#  it is an opeartor overloading(Polymorphism)

class Complex :
    def __init__(self,real,img):
     self.real = real
     self.img = img 
    
    def showNumber(self):
       print(self.real,"i +",self.img,"j+") 
    
    def  __add__(self,num2):
       newReal = self.real+num2.real
       newImg = self.img + num2.img 
       return complex(newReal,newImg)
   
    def  __sub__(self,num2):
       newReal = self.real-num2.real
       newImg = self.img - num2.img 
       return complex(newReal,newImg)



num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
print(num3)

num3 = num1 - num2
print(num3)
