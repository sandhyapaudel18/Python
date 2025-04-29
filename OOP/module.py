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
# print(s1.get_marks())

#practice questions
class People:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    
    def get_average(self):
        sum=0
        for i in range(len(marks)):
            sum += marks[i]

        avg=sum/len(marks) 
        return avg   
            


marks=[34,35,56]
s1=People("sandhya",marks)
print("hey sandhya your average is ",s1.get_average())