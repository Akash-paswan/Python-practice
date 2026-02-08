class Student:
    college_name = "ABC College"
     
    def __init__(self, name,marks):  # comstructor
        self.name = name    
        self.marks = marks     

#    methods 
    def welcome(self):    # hmne ek method banaya hai jisme sabse pehle self ko welcome ke andar likhna padega 
     print("welcome student")   #   method bhi ek type ka function hi hai 

    def get_marks(self):
        return self.marks 
    # objects 
s1 = Student("karan",92)
s1.welcome()
print(s1.get_marks())