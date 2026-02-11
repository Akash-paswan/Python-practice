#  ques no 1 
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius 
    
#     def area(self):
#         return (22/7)* self.radius**2
     
#     def perimeter(self):
#         return 2 * (22/7) * self.radius         

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

#  ques no 2 
# class Employee:
#     def __init__(self,role,dept,salary):
#      self.role = role
#      self.dept = dept
#      self.salary = salary
     
#     def showDetails(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)
        
         
         
# class Engineer(Employee):
#     def __init__(self, name,age):
#         self.name = name 
#         self.age = age 
#         super().__init__("Engineer","IT","75000")
        
        
# engg1 = Engineer("Elon Musk",40)
# engg1.showDetails()       
            
  #  ques no 3 
   
class order :
    def __init__(self,item,price):
        self.item = item 
        self.price = price
        
    def __gt__(self,ord2):
        return self.price> ord2.price
        
        
ord1 = order("chips",20) 
ord2 = order("tea",15)


print(ord1>ord2) # true 
                 
         