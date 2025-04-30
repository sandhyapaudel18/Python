#trying to change class level attributes
# class Person:
#     name="sandhya"

#     def changeName(self,name):
#      self.__class__.name=name
#      #self.__class_.attribute=class name only

# p=Person()
# p.changeName("paudel")
# print(p.name)  
# print(Person.name)     


#next way
class Student:
   name="virat"
   @classmethod
   def changename(cls,name):
    cls.name=name
    print(cls.name)


c=Student()
c.changename("sandhya")