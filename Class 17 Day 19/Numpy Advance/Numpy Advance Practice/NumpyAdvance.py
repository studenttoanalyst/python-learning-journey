# Ek Simple List Banao (Array)
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr)

# Reshape Karna (Line ko box bana do)
arr = np.array([9,8,7,6,5,4,3,2,1,0])
new_shape = arr.reshape(2,5)
print(new_shape)

# Masking (Filter Lagana)
arr = np.array([10,20,30,40,50,60,70,80])
result = arr[arr>20]
print(result)

# Broadcasting (Sab pe ek sath kaam)
arr = np.array([1,2,3,4,5])
result = arr+5
print(result)

# Random Numbers Banana
arr = np.random.randint(1,100,size=(3,3))
print(arr)

# Aggregation (Jama, Average, Max)
arr = np.array([1,2,3,4])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))