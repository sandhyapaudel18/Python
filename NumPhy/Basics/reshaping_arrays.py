#changing the dimension of array without affecting datas
import numpy as np
arr=np.array([2,3,4,6,7,4])
new_arr=arr.reshape(3,2)
# print(new_arr)
#reshaing doesnot create copy it returns a view
#changes only view


#flattening arrays=changing 3 dimensional arrays into 1 dimensional array

#ravel()=returns view , affects original value
#flatten()=returns copy , only shows copy not real one


arrays=np.array([[1,2,3],
                 [4,5,6]])
print(arrays.ravel()) #only view and affects
print(arrays.flatten())