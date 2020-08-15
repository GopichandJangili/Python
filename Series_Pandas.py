import pandas as pd
import numpy as np
#######Pandas Series############
################################
################################
###    pd.Series( data, index, dtype, copy)  ---> S is capital in series

### use s for series and df for dataframe

#1. Declare Empty Series
a = pd.Series(dtype='float64')
print(a)

#2. Series form dict
test_dict = {'a':1,'b':2}
c = pd.Series(test_dict)
print(c) ###Keys will become index

#3. Seroies from scalar value
a =pd.Series(3,index=[1,2,3])
print(a)

#4. Create a series from list
a = [1,2,3]
x = pd.Series(a)
print(x)
print(list(x))   ##Converting a list to pandas series

#5. Null value in python is created using numpy
s = pd.Series([1,2,3,np.nan])
print(s)

#6. Combine two series to create a dataframe
s1 = pd.Series([1,2,3,4],dtype='int32')
s2 = pd.Series([5,6,7,8])
df = pd.concat([s1,s2],axis=0,ignore_index=True)
df_index = pd.concat([s1,s2],axis=0,ignore_index=True)
df_new = pd.concat([s1,s2],axis=1)
print(df,df_index,df_new)

#7. Series vs list vs Array

a = np.array([1,2,3])
b = list(a)  # a.tolist()    Converting numpy array to list
num_array = np.array(b)
print(num_array) 
c = pd.Series(a)
print(a,b,c)


### range function
a = range(5)
b = range(1,5)
c = range(1,5,2)   # 2 indicates step
print(list(a),list(b),list(c))

#8. series
s = pd.Series(3,range(5),dtype='float32')
print(s)

#9 series copy
s = pd.Series([1,2,3,4])
s1 = s.copy()
print(s1)

####10 Accessing -  using indexes and position

a = np.array([1,2,3])
s = pd.Series(a,index=[7,7,9])
print(s[7],s[:1])   
d1 = {'a':1,'b':2}
s1 = pd.Series(d1)
print(s1)
d2 = {'b':1,'a':2,'c':4}
s2 = pd.Series(d2)
print(s2)
s3 = s2.astype(float)
print(s3)

####11 Transpose returns self
s = pd.Series([1,2,3,4])
p = s.transpose()
print(s)
print(p)
