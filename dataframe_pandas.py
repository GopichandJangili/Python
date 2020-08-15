#############################
############DataFramme#######
#############################
import pandas as pd
import numpy as np

#NULL example
l = [1,2,np.nan]
print(l)

#pd.DataFrame( data, index, columns, dtype, copy)

#1. Empty DataFrame
df = pd.DataFrame()
print(df)

#2. DataFrame from list
l1 = [1,2,3]
df = pd.DataFrame(l1)
print(df)
#to list
l2 = df[0].tolist()
l3 = df[0]
print(l2,type(l3))

#3. Dataframe from list od lists
l = [['a',2],['b',4],['c',6]]
df = pd.DataFrame(l,columns=['A','B'],dtype='float')
print(df)

#4. Dictionary to DataFrame
d1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
df = pd.DataFrame(d1)

#5. Giving indexex
l1 = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(l1,index=['a','c','z'])

#6. DataFrame from list of dicts
a = [{'a':1,'b':2},{'a':3,'c':5,'d':8}]
df = pd.DataFrame(a)
print(df) 

#7. dict of series
a = {'a':pd.Series([1,2,3]),'b':pd.Series([1,2,3,4])}
df = pd.DataFrame(a)
print(df)

#8. Adding third column from existing 2 columns in DataFrame
a = {'a':pd.Series([1,2,3,4]),'b':pd.Series([1,2,3,4])}
df = pd.DataFrame(a)
df['c'] = df['a']+df['b']
print(df)

#9. Case statement in DataFrame
df = pd.DataFrame([[1,2,3],[3,4,5]],columns=['a','b','c'])
print(df)
def func(row):
    if row['a'] == 1:
        return 'mobile'
    elif row['a'] ==3:
        
        return 'abcd'
    else:
        return 'other'

df['third'] = df.apply(func, axis=1)
print(df)


