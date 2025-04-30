#broadcasting=way of performing operations on different shape arrays
#without loops
import numpy as np
prices=np.array([100,900,800])
discount=10  #scalar value

#broadcasting 
final_prices=prices-(prices*discount/100)
# print(final_prices)

result=prices * 2
# print(result)


#shapes=different dimensions diff rows and columns
matrix=np.array([1,2,3,4,5,6,7,8])
vector=np.array([[2,3,4,6],
                [6,7,8,9]])
matrix_new=matrix.reshape(2,4)
result=matrix_new + vector #cannot perform this as its of incompatible shapes

print(result)

#vectorisation = applying conditions on arrays without loops

# list1=np.array([1,2,4])
# list2=np.array([3,4,5])

# result= list1+list2
# print(result)

# arr=np.array([5,6,6])
# mul=arr * 5
# print(mul)

#broadcast= change smaller arrays to larger arrays to make them of same shape and perform tasks eg 1d to 2d
#vectorisation= can perform operations in entire array without loops,eg matrix op