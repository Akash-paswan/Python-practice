# f = open("demo.txt",'w')

# f.write("i want to learn pandas from apna college")

# f.close()


# f = open("smaple.txt","a")

# f.write("i want to learn python from apna college")
# f.close()


# f = open("smaple.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()



# f = open("smaple.txt","w+")
# # f.write("abc")
# print(f.read())
# f.close()



with open("demo.txt","r") as f :
 data = f .read()     # jab hmlog with syntax ka use karte hai to f.close ka use karna jaruri nhi (compulsory nhi hai )wo automatic ho  jata hai 
print(data)