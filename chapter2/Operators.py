#  Arithmetic operator
a= 5
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  # modulo(%) remainder ki value batata hai
print(a**b)  # a^b ki value battata hai

  # Rrlational operator 
a= 50
b = 20
print(a==b) # False
print(a !=b) # true
print(a>=b)  # True
print(a>b)   # True
print(a<b)  # False
  
  # Assignment operator 
num = 10
# num = num+10
num+=10  # 23 and 24 line ka same matlab hota hai
print("num is :",num)
 
#   ekm uar example
num = 10
num *= 10
print(num)

#  ek aur 
num = 10
num **= 5
print(num)

# logical opeator
a = 50
b = 30
print(not False)
print(not a>b)   # not operator kewal one operands per kewal per kaam karta hai

#   And operator
val1 = True      # and operator two operands per kaaam karta hai 
val2 = True # operator tabhi kaam karta hai ja dono value shi hi tabhi 
# print("And operator",val1 and val2) 

print("or operatopr", val1 or val2)  # Or operator tabhi kaam karta hai dono me koi  ek bhiu shi rh to value will bhi true 
print("Or operator",(a==b or(a>b)))