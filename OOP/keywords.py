

#del= to delete the objects
#del s1 - direct object delete
#del s1.name- deletes only name of s1 object


class Student:
    def __init__(self,name):
        self.name=name


s1=Student("sandhya")
print(s1.name) 

del s1.name
print(s1.name)