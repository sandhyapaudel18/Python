#print even numbers between 1 to 10 and at last print [We have 4 even numbers]
# for number in range(1,10,1):
#     if number%2==0:
#         print(number)

# print("We have 4 even numbers ")       

#wap to ask user to enter their 3 favourites movie and store in movies

movies =[]
# for i in range(3):
#     movies.append(input("enter name"))
# print(movies)


#wap to check if list contains palindrome of elements
# [1,2,3,2,1] [1,"abc","abc",1]

name=[1,2,3,2,1]
m=[]
m=name.copy()
m.reverse()
if m==name:
    print("palindrome")
else:
    print("not palindrome")

