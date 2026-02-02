# #  ques no 1 
# num = [1,4,9,16,25,36,49,64,81,100]
# for val in num :
#     print(val)

#  ques no 2 
tup = (1,4,9,16,25,36,49,64,81,100)
x = 25

idx = 0
for el in tup:
    if(el == x):
        print("number found at idx",idx)
    idx += 1 