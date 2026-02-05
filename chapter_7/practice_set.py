#  ques 1 
# with open(" practice.txt","w") as f :    
#   f.write("hi everyone\nwe are learning file I/O")
#   f.write("using java \n I like programming in java ")



#  ques 2 
# with open(" practice.txt","r") as f :    
#        data = f.read()
       
#        new_data = data.replace("java","python")
#        print(new_data)    
       
       
# with open(" practice.txt","w") as f :    
#        f.write(new_data)                

#  ques 3 

word =" learning "
# with open("practice.txt","r") as f :
with open(" practice.txt","r") as f :
    data = f .read()
    if(data.find(word) != -1):
        print("FOUND")
    else :
        print("NOT FOUND ")