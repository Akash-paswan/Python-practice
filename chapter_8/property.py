# class Student:
#     def __init__(self,phy,chemi,math):
#         self.phy = phy
#         self.chemi = chemi
#         self.math = math
#         self.percentage = str((self.phy+ self.chemi+self.math) /3)+ "%"
        
#         # def calcPercentage(self):
#         #  self.percentage = str((self.phy, self.chemi,self.math) /3)+ "&"
  
  
# stu1 = Student(98,97,99)
# print(stu1.percentage)





# maanlo hme physics ke number me change karna hai to 98 ki jaghah oer 86 likhna hai to hme ek naya method banayenge 
 
# class Student:
#     def __init__(self,phy,chemi,math):
#         self.phy = phy
#         self.chemi = chemi
#         self.math = math
#         self.percentage = str((self.phy+ self.chemi+self.math) /3)+ "%"
        
#     def calcPercentage(self):
#      self.percentage = str((self.phy+ self.chemi+self.math) /3)+ "%"
  
  
# stu1 = Student(98,97,99)
# print(stu1.percentage)


# stu1.phy =86
# print(stu1.phy) 
# stu1.calcPercentage() 
# print(stu1.percentage)        # isko ham aur simple methods se kar skte haiu jaise propertty decorator se 

#   use property decorator  
class Student:
    def __init__(self,phy,chemi,math):
        self.phy = phy
        self.chemi = chemi
        self.math = math
        
        
    @property
    def percentage(self):
        return str((self.phy+ self.chemi+self.math) /3)+ "%"
        
  
  
stu1 = Student(98,97,99)
print(stu1.percentage)


stu1.phy =86
print(stu1.percentage)
