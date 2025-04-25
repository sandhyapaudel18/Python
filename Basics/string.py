str="sandhya"
print(len(str))

print(str[0])
# -1 represents the end of the string
# print(str[-1])
# print(str[0:])
# print(str[:])

# escape character after
course ="sandhya \' paudel"
abc="sandhya \\ Program"
abc="sandhya \n Program"
# print(abc)



str1="sandhya"
str2="paudel"
bull=f"{len(str1)} {len(str2)}"
full=str1 + "" +str2
print(bull)


#string methods
course ="bca nepal    "
print(course.upper())
print(course.lower())
print(course.title())
#strip= removes start and end white spaces
print(course.strip())
print(course.find("Ca"))
#-1= not found
print(course.replace("a", "j"))
#gives true or false
print("a" not in course)
