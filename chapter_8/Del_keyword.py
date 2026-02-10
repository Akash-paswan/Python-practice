# class Student:
#     def __init__(self,name): 
#         self.name = name
        
       
# s1 = Student("Shradha")
       
# del s1        #     isme error aayega bcz hmne pehle del keywored ka usw kiyua hai 
# print(s1) 
        
        
class Student:
       def __init__(self,name):
        self.name = name
        
s1 = Student("Shradha")
print(s1.name)
del s1.name    
print(s1.name)  