import sys

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

'''#How to make a python function that handles scalars to work on numpy arrays
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(pair_max(a, b))'''
'''
#How to swap two columns in a 2d numpy array

arr = np.arange(9).reshape(3,3)
print(arr)

print(arr[:, [1,0,2]])'''

'''#How to swap two rows in a 2d numpy array
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[[1,0,2]])'''

'''#How to reverse the rows of a 2D array
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[::-1])'''

'''#How to reverse the columns of a 2D array
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[:,::-1])'''

'''#How to create a 2D array containing random floats between 5 and 10
rand_arr = np.random.uniform(5,10, size=(5,3))
print(rand_arr)
rand_arr_a = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
print(rand_arr_a)'''

'''#How to print only 3 decimal places in python numpy array
rand_arr = np.random.random([5,3])
print(rand_arr)
np.set_printoptions(precision=3)
print(rand_arr)
#print(rand_arr[:4])
'''

'''#How to pretty print a numpy array by suppressing the scientific notation (like 1e10)
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
np.set_printoptions(suppress=True)
print(rand_arr)'''

'''#How to limit the number of items printed in output of numpy array
a = np.arange(15)
print(a)
np.set_printoptions(threshold=6)
print(a)'''

'''#How to print the full numpy array without truncating
np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)
#import sys in above
#np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=len(a))
print(a)'''

'''#How to import a dataset with numbers and texts keeping the text intact in python numpy
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris[:3])
iris = np.genfromtxt(url, delimiter=',', dtype=None, encoding='UTF-8')
print(iris[:3])'''

'''#How to extract a particular column from 1D array of tuples Not Understand
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None, encoding='UTF-8')
print(iris_1d[:3])
print(iris_1d.shape)
species = np.array([row[4] for row in iris_1d])
print(species[:5])'''

'''#How to convert a 1d array of tuples to a 2d numpy array
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None, encoding='UTF-8')
print(iris_1d[:4])

# Method 1: Convert each row to a list and get the first 4 items
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
print(iris_2d[:4])

# Alt Method 2: Import only the first 4 columns from source url
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(iris_2d[:4])'''

'''#How to compute the mean, median, standard deviation of a numpy array
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
print(sepallength)
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(f'mean_value: {mu}, median_value: {med}, standard_deviation_value: {sd}')'''

'''#How to normalize an array so the values range exactly between 0 and 1
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
print(sepallength)
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/sepallength.ptp()
#ptp preserves the data type of the array.
#This means the return value for an input of signed integers with n bits (e.g. np.int8, np.int16, etc)
np.set_printoptions(precision=3)
print(S)'''

'''#How to compute the softmax score
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.array([float(row[0]) for row in iris])

# Solution
def softmax(x):
    """Compute softmax values for each sets of scores in x.
    https://stackoverflow.com/questions/34968722/how-to-implement-the-softmax-function-in-python"""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

print(softmax(sepallength))
print(sum(softmax(sepallength))+0.0000000000000001)'''

'''#How to find the percentile scores of a numpy array
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

ans = np.percentile(sepallength, q=[5, 95])
print(ans)
#print(np.percentile(sepallength, q=[20, 80]))'''

#How to insert values at random positions in an array
'''rrr = np.arange(10).reshape(2,5)
print(rrr)
#method 1
i, j = np.where(rrr)
print(i,j)
np.random.seed(100)
rrr[np.random.choice((i), 5), np.random.choice((j), 5)] = 9999
print(rrr)
#rrr[0, 1] = 9999
#print(rrr)'''
'''print(np.where([ [True, False]],
               [[1, 2]
              , [3, 4]],
               [[5, 6],
                [7, 8]]))'''

'''#find the position of missing values in numpy array
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(iris_2d)
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

# Solution
print("Number of missing values: \n", np.isnan(iris_2d[:, 0]).sum())
print("Position of missing values: \n", np.where(np.isnan(iris_2d[:, 0])))
'''

#drop rows that contain a missing value from a numpy array
'''url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
#print(iris_2d)
any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
pp = iris_2d[any_nan_in_row][:5]
print(pp)'''

#find the correlation between two columns
'''url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

pp = np.corrcoef(iris[:, 0], iris[:, 2])[0, 1]
print(pp)'''

#find if a given array has any null values
'''url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

# Solution
iris_2d[np.isnan(iris_2d)] = 0
print(iris_2d[:4])'''

