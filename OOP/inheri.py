# class Car:

#     def can_drive(self):
#         print("Can drive the car")


# class Toyota(Car):

#     def high_mileage(self):
#         print("gives high mileage")    


# class Main():
#     toy=Toyota()
#     toy.high_mileage()
#     toy.can_drive()



# class CCar:
#     @staticmethod
#     def can_ddrive(name):
#         print("with static method1", name)   


# class Porsche(CCar):
#     @staticmethod
#     def high_mileagee():
#         print("static method mileage one")

# class Program:
#     Porsche.can_ddrive("sandhya")
#     Porsche.high_mileagee()        


#multiple inheritance
#can extend from two diff classes

class A:
    vara="welcome to a"
class B:
    vara="welcome to b"
class C(A,B):    
    varc="welcome to c"
class Main:
    c= C()
    print(c.vara)
    print(c.vara)
    print(c.varc)    


#super keyword super()=>to access elements from parent class
class D:
    def show():
        print("hello")
 


class F(D):
   def __init__(self):
       super().__init__()
   
         