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

# print(np.vstack((arr3,arr4)))
print(np.hstack((arr3,arr4)))