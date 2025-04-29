# class Student:
#     name="sandhya"
#     age="10"

# s1=Student()
# print(s1.name)    

# s2=Student()
# print(s2.name)

# class Cars:
#     name="honda"

# c1=Cars()
# print(c1.name)    

#constructors
class Cars:
 def __init__(self): #default
      pass
      
      #parameterized constructors
      #self.=diff objects have different values
 def __init__(self,name): #name attribute jun user gave via constructor
        self.name=name #self wala object lai refer garne
        

c1=Cars("honda")
c2=Cars("porsche")

#class and instances attributes
# class.atr = common for all
# obj.atr= unique for all, priority over class attributes

class Student:
    college_name="bkc"
    
    def __init__(self,name):
        self.name=name
        

s1=Student("sandhya")  
print(s1.name)  


