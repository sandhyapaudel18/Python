#accessing elements in an array
import numpy as np
arr=np.array([1,4,5,3,2])
print(arr[0])
print(arr[-1])

#extracting the sub array from anarray
print(arr[0:3:1]) #slicing here start,stop,steps and stop-1 huncha
print(arr[::-1]) #reversing array elements

#fancy indexing
news=np.array([5,6,3,4,2])
print(news[[0,3,2]]) #extracting multiple elements at once here called fancy indexing


#boolean masking
print(news[news>4])