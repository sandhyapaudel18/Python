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
array_3d_app=np.append(array_2d,67)

array_2d_new=np.insert(array_2d,1,45,axis=None)
# print(array_2d)
# print(array_2d_new)
# print(array_3d_app)


#merging two arrays
# arr=np.array([[1,2,3],
#              [7,8,9]])
# arr2=np.array([[4,5,6],
#               [7,5,4]])
# array_merged=np.concat((arr,arr2),axis=1)
# print(array_merged)

"""
removing elements in array use delete()
np.delete(index) in new array original remains same

"""
arr1=np.array([1,2,5,6,7,7])
arr2=np.delete(arr1,0)
print(arr2)


arr=np.array([[1,2,3],
             [7,8,9]])
arr2=np.array([[4,5,6],
              [7,5,4]])

arr3=np.delete(arr,0,axis=0)
print(arr3)