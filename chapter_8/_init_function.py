# class Student:
    
#     def __init__(self, fullname):
#         self.name = fullname     # isme jo fullname likha hai wo name hai jo parameter me name hai 
#           # aur jo self.name hai jo wo object ke andar jo kuch naya create hone wala hai
#         print("adding new students in database")

# s1 = Student("karan")
# print(s1.name)


# s2 = Student("akash")
# print(s2.name)






class Student:
    
    #  default constructor 
      def __init__(self):    # iska hm use tabhi karte hai jab hme parametrised constructor ka use no jab dodno chalege call argument uski  syngega jiska parametr pass kiya hoga  
             pass
    
    #  this is a paramerterised constructor
      def __init__(self, name,marks):
        self.name = name
        self.marks = marks     
        print("adding new students in database")

s1 = Student("karan",92)
print(s1.name, s1.marks)


s2 = Student("akash",88)
print(s2.name, s2.marks)
