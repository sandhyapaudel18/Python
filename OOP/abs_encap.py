#abstraction =hiding the implementation of details of class and showing imp features to the users
#example:we donot know how engine works behind the scenes of driving cars


#encapsulation=wrapping data and functions in the single unit
class Account:
    def __init__(self,account_num,balance):
        self.account_num=account_num
        self.balance=balance


    def debit(self,amount):
        self.balance -= amount
        return self.balance
    
    def credit(self,amount):
        self.balance += amount
        return self.balance
    
    def balance_show(self):
        print(self.balance)


a1=Account(10,10000)
print(a1.debit(100)) 
print(a1.credit(1000))

a1.balance_show()    