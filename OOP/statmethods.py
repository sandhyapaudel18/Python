class Student:
    #static method donot use self
    def __init__(self,name):
     self.name=name


    @staticmethod
    def get_marks():
        print("name is ")


ss= Student("AKASH")        
ss.get_marks()