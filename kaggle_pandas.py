import pandas as pd
import numpy as np

#print(pd.__version__)
'''#How to create a series from a list, numpy array and dict
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
sa = pd.Series(mylist)
sb = pd.Series(myarr)
sc = pd.Series(mydict)
#print(sc)'''
'''#How to convert the index of a series into a column of a datafram
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
df = ser.to_frame().reset_index()
print(df)'''
'''#How to combine many series to form a dataframe
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df = pd.concat((pd.DataFrame(ser1),pd.DataFrame(ser2)),axis=1)
print(df)
# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})'''

'''#How to assign name to the series’ index
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.name = 'alphabets'
print(ser)'''
'''#How to get the items of series A not present in series B
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
#serB = ser1.isin(ser2)
serC = ser1[~ser1.isin(ser2)] # ~ NOT Inverts all the bits
print(serC)'''
'''#How to get the items not common to both series A and series B
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser_u = pd.Series(np.union1d(ser1, ser2))  # union
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
result = ser_u[~ser_u.isin(ser_i)]
print(result)
#Solution 2(me)
ss = ~ser1.isin(ser2)
rr = ~ser2.isin(ser1)
print(pd.concat((ser1[ss],ser2[rr]),axis=0))'''
'''#How to get the minimum, 25th percentile, median, 75th, and max of a numeric series
#ser = pd.Series(np.random.normal(10, 5, 25))
#print(ser)
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))
arr = np.percentile(ser, q=[0, 25, 50, 75, 100])
print(arr)'''
'''a =[10,20]
print(np.percentile(a,q=[50]))'''
'''#How to get frequency counts of unique items of a series
ser = pd.Series(np.take(list('abcde'), np.random.randint(5, size=10)))
print(pd.DataFrame(ser.value_counts()).reset_index())'''

'''#How to keep only top 2 most frequent values as it is and replace everything else as ‘Other
#np.random.RandomState(100)
#ser = pd.Series(np.random.randint(1, 5, [12]))
ser = pd.Series(np.take(list('abcde'), np.random.randint(5, size=10)))
#ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
print(ser.value_counts())
print("---")
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
print(ser)'''

'''#How to bin a numeric series to 10 groups of equal size
ser = pd.Series([10,11,40,30])
print(ser)
qc = pd.qcut(ser, q=[0, 0.25, .5, .75, 1],
        labels=['1st_quater','Half_quater','3rd_quater','Full'])

print(qc)'''
'''#How to convert a numpy array to a dataframe of given shape
ser = pd.Series(np.random.randint(1, 10, 35))
df = pd.DataFrame(ser.values.reshape(7,5))
print(df)'''

