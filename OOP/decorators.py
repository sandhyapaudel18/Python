class Student:
    def __init__(self,name,phy,ch,bio):
        self.name=name
        self.phy=phy
        self.ch=ch
        self.bio=bio
        
        

    # def cal_percentage(self):
    #     self.percentage=str((self.phy+self.ch+self.bio)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.ch+self.bio)/3)+"%"

c=Student("sandhya",10,28,39)
print(c.percentage)