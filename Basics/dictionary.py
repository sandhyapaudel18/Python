#stores data in key:value pair form
#unorderd,mutable,but not duplicate value like list does

info={
    "name":"sandhya",
    "gpa":10,
    "age":21 ,  
    "is_logged":True,
    "ll" :[1,2,3,4,5],
    "tt":("sandhya","paudel"),
    12:"data"
}
info["name"]="paudel"
null_dict={}
# print(null_dict)


# print(student["subjects"]["dsa"]) to access dict-dict-item
#methods .keys()=only keys
#.values()=only values
#.items()=return all key and value as tuples
#.get("key_name")=value as per keys
#.update(newItem)=inserts new item to the dictionary

student={
    "name":"akash",
    "subjects":{
        "dsa":99,
        "os":67
    }
}
# print(student.values())
# print(list(student.keys()))
# print(len(student))
# print(student.items())
print(student.get("name")) #none if is no any kay
print(student["name"]) #error if there is no any key and no execution of code after this
# print(tuple(student.items()))
student.update({"city":"sunwal"})
print(student)
#override huncha ani duplicate keys hunna