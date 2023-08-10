import numpy as np
arr=np.array([1,2,3,4,5])
filtered_arr=np.array(list(filter(lambda x: x % 2 !=0,arr)))
print("Filter Program")
print(filtered_arr)