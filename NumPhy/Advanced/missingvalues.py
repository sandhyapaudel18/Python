#why to find missig values?
import numpy as np
#np.isnan = detects missing values in dataset

arr=np.array([3,4,2,4,np.nan,-np.inf])
# print(np.isnan(arr))
#cannot compare 
# print(np.nan == np.nan)

#np.nan_to_num(arr,nan=value) default=0
# new_one=np.nan_to_num(arr,nan=9)
# print(new_one)

#handling infinite values
#np.isinf() : divide by 0 aor power by 1000

new_arr=np.isinf(arr)
print(new_arr)

array=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(array)