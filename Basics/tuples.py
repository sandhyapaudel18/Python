#immutable sequences of values
tuple=(1,) #why comma because py thinks it as normal interger insitead of tuples so use comma
# print(tuple)

tconcept=(4,5,34,3)
# print(tconcept.index(5))

# print(tconcept.count(5))
#tuples questions here
#wap to count the number of students with A

tt=("C","D","T","Y","C","C")
# print(tt.count("C"))


ll=[]
for i in range(len(tt)):
    ll.append(tt[i])
ll.sort()    
print(ll) 
  