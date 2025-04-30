import numpy as np
num_arr=np.array([1,2,3,4,5])
print(num_arr)

nums_2array=np.array([[1,2,4],
                      [4,5,6],
                      [6,7,8]])
print(nums_2array)

#one dimensional=single row
#two dimensional=one row and one column
#three dimensional=three points x,y,z

#creation of array from list

#1:np.arrayfucntion()

arr=np.array([2,3,4,4])
print(arr)
#2:0s functions

array=np.zeros((3,3)) #only for 0
print(array)

arrs=np.ones((2,1)) #only for 1
print(arrs)

a=np.full((3,3),7)
print(a)