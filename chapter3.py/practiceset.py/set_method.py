# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("apnacollege")   # create string in set 
# collection.add((1,2,3,))   # tuple ( set le andar tuple create kaqqr skte hai )
# # collection.add([1,2,3,])    # bvut set ke andar list nhi create kar skte hhai 
 

# collection.remove(3)

# print(len(collection))
# print(collection)

#     naya program 
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("apnacollege")   # create string in set 
# collection.add((1,2,3,))

# collection.clear()    # iska baad length ka set ka vlaue 0 ho jayegaq 
# print(len(collection))

#    .pop means remove ya delete a random value 
# collection = {"hello","apna college","world","coding","python",}
# print(collection.pop())
# print(collection.pop())


# most important  set in union and intersection 
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))    #{1,2,3,4}
print(set1) 
print(set2) 
print(set1.intersection(set2))    #{2,3}