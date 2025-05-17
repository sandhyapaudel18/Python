def sum_numbers(f_name,s_name):
    print(f" hello {f_name} {s_name}")



sum_numbers("sandhya","paudel")


#types of functions
def sum(x):
    return f"{x+1}"


print(sum(10))


#key words arguments
def increase(x,by):
    return x+by


print(increase(20,by=9))


#default arguments the optional para must be at last
def increase(x,by=1):
    return x+by


print(increase(20,4))

#args
def multiply(*numbers):
    mul=1
    for number in numbers:
        mul *=number

    return mul

result=multiply(3,4,5,6)
print(result)

 
def subs(a,b):
    return a-b;

print(subs(10,30))
 





