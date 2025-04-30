#stacking , combining arrays either horizontally or vertically 
#vertical=rows=vstack()
#horizontal=column=hstack()
import numpy as np
arr1=np.array([1,2,4,5])
arr2=np.array([6,7,4,2])

# print(np.vstack((arr1,arr2)))
# print(np.hstack((arr1,arr2)))


arr3=np.array([[1,2,3],
              [4,5,6],
              [6,7,8]])
arr4=np.array([[3,2,1],
              [6,5,4],
              [8,9,0]])

# print(np.vstack((arr3,arr4))) #layering just adds at last
# print(np.hstack((arr3,arr4))) #col1 - col2 like this


#splitting = creating equal sub arrays of given array
arr0=np.array([1,2,4,5,6,4])
print(np.split(arr0,3))