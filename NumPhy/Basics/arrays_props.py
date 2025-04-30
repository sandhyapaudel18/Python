#array operations
import numpy as np
arr=np.array([[1,2,3,4],
              [4,5,6,7]])

print(arr.shape) #knowing shape
print(arr.size) #total elements in an array
print(arr.ndim)  #to know number of dimension either 2 or 3d

arrays=np.array([1,2,3,89.009])
print(arrays.dtype)  #to know the data type


#change the data type into another data type
int_arrays=arrays.astype(int)
print(int_arrays)
print(int_arrays.dtype)


