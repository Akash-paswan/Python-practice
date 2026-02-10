#  this is a public attributes 
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass
        
# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.acc_pass)

#  this is a private attributes ya methods 
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
        
#         # def reset_pass(self):
#         #      print(self.acc_pass)     #  private attribute hide kar deta hai personal cheejhi ko jaiswe isme acc_pass ko hide karke sirf acc_-no show kiya hai 
        
# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.__acc_pass)



class Account:
    def __init__(self,acc_no,acc_pass):
     self.acc_no = acc_no
     self.__acc_pass = acc_pass

        
    def reset_pass(self):
     print(self.__acc_pass)





acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.reset_pass())