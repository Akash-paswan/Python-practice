student= {
    "name": "akash paswan",
        "subjects": {
            "phys":97,
            "chemi":98
        
    }
}
# print(len(student))          # len of dict to total no of key value btata hai 
# print(list[student.keys()])
# print([student.keys()])
# print([student.values()])
# print(list[student.values()])
# print(student.items())
# print(list(student.items()))

# pairs = list(student.items())   
# print(pairs[0])
# print(pairs[1])

print(student["name"])
print(student.get("name"))

#  if we write 
# print(student["name2"])      # it will be return error
print(student.get("name2"))    # return none vaue     
 
new_dict = {"name":"prakash paswan","age":22}
student.update(new_dict)
print(student)          