#for loop
for number in range(1,10,2):
    print(number* "*" )


#for else
success=False
for number in range(4):
    print("Try")
    if success:
        print("we tries and happened at",number)
        break
    else:
        print("tried but didnot get up to",number)  
        break
 #nested loops
# for number in range(3):
#     for number2 in range(4):
        # print(f"{number}")              

#iterables

# shopping_Cart=["sandhya","paudel"]
# for items in shopping_Cart:
#     print(items)

#while loops
# x=4
# while x>0:
#     print(x+2)
command=""
while command.lower() !="quit":
    command=input(">")
print("ECHO",command)   

#infinite loops

