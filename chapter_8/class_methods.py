# class Person:
#     name = "anonymous"
    
#     def changename(self,name):              
#         # self.name = name    # yah statement likhn se ek naya name crete hua hai but hme to class attribute change karna hai ( isme jo self hai uska matlb object hota hai )
#         # Person.name=name   ye bhi thik hai but hm dustra kuch try karenge 
#         self.__class__.name= "akash paswan"
#         #  self.__class__.person.
        
        
        
        
# p1 = Person()
# p1.changename("akash paswan")
# print(p1.name)      
# print(Person.name)  



class Person:
    name = "anonymous"
    
    @classmethod
    def changename(cls,name):
        cls.name = name 
    
    
    
    
p1 = Person()
p1.changename("akash paswan")
print(p1.name)      
print(Person.name)  

