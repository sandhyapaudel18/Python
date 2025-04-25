#arithmetic operator
a=10
b=10
if a>b:
    print("a is greater")
    print("hey")

elif  b == a:
    print("both are equal")   
print("hello")    


#ternary operator
c=10
d=90
result="c is greater" if c>d else "d is greater" #its ternary operator
print(result)

#and/or operator
high_income=True
good_credit=True 
student=True

if(high_income and good_credit and not student):
    print("Eligible to get loan")

else:
    print("Not Eligible")

#IF(COND1 or COND2):
#print("Its or opertor used right here")

#short circuit meaning starts with first args and check 
# second step by stey if one args is value the evaluation stops
