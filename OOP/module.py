class Student:
    college_name="bkc"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        pass

    def hello(self):
        print(self.name)

    def get_marks(self):
        return self.marks



s1=Student("sandhya",10)
s1.hello()
print(s1.get_marks())
