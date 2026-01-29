info = {
    "name": " apna college",
    "subject":["python","pandas","metpotlib",],  # ek list store kiye hai 
    "topics": ("dict","set"),      # tuples 
    "key": "value",
    # "name":" apnacollege",  #    dictionar me keys ko ek hhi var likh skte hai do baar name key likh nhi akte hai 
    "learning":"coding",
    "age": 35,
    "is adult": True,
    "marks":94.4,
    }
info["name"]= "akashpaswan"   # overwrite
print(info["name"])
print(info["topics"])
print(info["key"])
print(info["learning"])
print(type(info)) 

#  hm ek naull dict ko bhi create kar skte hai 
null_dict = {}
null_dict["name"]= "apna college"
print(null_dict)
