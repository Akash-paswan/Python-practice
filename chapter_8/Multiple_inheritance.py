class A :                              #  parent class 
    varA = "welcome to class A"
  
class B:                                 # another parent class 
    varB= "welcome to class B "
    
class C(A,B) :                              #   child class 
    varC = "welcome to class C"
    
c1 = C()                             #create object

print(c1.varC)
print(c1.varB)
print(c1.varA)

           