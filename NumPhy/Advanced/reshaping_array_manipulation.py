#add,remove,stack,split,merge
#numpy array has fixed size,static in nature to add just create new array
#to add elements= np.insert(array,index,value,axis)
#axis=1: column wise
#axis:0 : row wise

import numpy as np
arr=np.array([1,2,3,4])
arr_new=np.insert(arr,0,10)

array_2d=np.array([[1,2,3],
                  [4,5,6]])

array_2d_new=np.insert(array_2d,1,45,axis=None)
print(array_2d)
print(array_2d_new)
