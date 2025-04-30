# class Student:
#     def __init__(self,name):
#         self.__name=name

#     def get_name(self): #to get private make function and just print
        # print(self.__name )

# ac=Student("sandhya")
# ac.get_name()



class Person:
    __name="unknow"
    
    def __hello(self): #such functions are used by some other internal fucntions within the class thats why they are used
        print("from private method")

    def get_value(self): #here we access private by calling private method from here
        print("from get method")
        self.__hello()    


#not happening cannot access from outside
# c1= Person()
# print(c1.__name)
# c1.__hello()

c1=Person()
c1.get_value()