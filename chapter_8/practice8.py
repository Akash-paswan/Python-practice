#   ya wla question phir se padhna hai 
class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
            print("hi",self.name,"your avg score is ",sum/3)
  
s1 =Student("akash paswan",[99,98,97])  
s1.get_avg()
#   hm isme attributes change bhi kar skte hai jaise name change kar diya 
s1.name = "ironman"
s1.get_avg()
                
       