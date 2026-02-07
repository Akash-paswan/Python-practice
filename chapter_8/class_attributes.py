class Student:
       college_name = "ABC College"
       name = "anonymous"    # class attributes
       def __init__(self, name,marks):
        self.name = name    # obj attributes 
        self.marks = marks      #   aur hmesha obj attri > class attributes
print(Student.college_name)   # class ek hi baar create krte hai  jabko obj to different baar likh skte haiu jaise self.name hai usme ham differnt naame create kara skte hai  
print("adding new students in database")

s1 = Student("karan",92)
print(s1.name, s1.marks)



