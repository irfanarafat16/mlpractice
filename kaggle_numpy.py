import numpy as np

#print(np.__version__)
'''a = np.arange(0,10,1)
print(a)'''
'''#How to create a boolean array
a = np.ones((3,3),dtype='bool')
print(a)'''
'''#How to extract items that satisfy a given condition from 1D array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr%2 == 1])'''
'''#How to replace items that satisfy a condition with another value in numpy array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 == 1] = -1
print(arr)'''
'''#How to replace items that satisfy a condition without affecting the original array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)'''
'''#How to reshape an array
arr = np.arange(10)
arr = arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols
arr = arr.reshape(5, 2)
print(arr)'''
'''#How to stack two arrays vertically
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
# Method 1:
print(np.concatenate([a, b], axis=0))
# Method 2:
print(np.vstack([a, b]))
# Method 3:
print(np.r_[a, b])'''
'''#How to stack two arrays horizontally
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
# Method 1:
print(np.concatenate([a, b], axis=1))'''
'''#How to generate custom sequences in numpy without hardcodin
a = np.array([1,4,3])
b = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(b)'''
'''#How to get the common items between two python numpy arrays
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))'''
'''#How to remove from one array those items that exist in another
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(a,b))
print(np.setdiff1d(b,a))'''
'''#How to get the positions where elements of two arrays match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where( a == b)
print(c)'''
'''#How to extract all numbers between a given range from a numpy array
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10)) #np.where return index
print(a[index])'''
#