#############################
############DataFramme#######
#############################
import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,2,3],'B':['4','5','6']})
#iterate over columns
for i in df:
    print(i)
#iterate over rows
for i in df.iterrows():
    print(i,list(i))

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
print(l2,type(l3))  # col of a DataFrtame is series

#3. Dataframe from list od lists
l = [['a',2],['b',4],['c',6]]
df = pd.DataFrame(l,columns=['A','B'],dtype='float')
print(df)

#4. Dictionary to DataFrame
d1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
df = pd.DataFrame(d1)
print(df)

#5. adding index
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

#9. Case statement in DataFrame (row wise)
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

#10. Case statement using lambda 
dict_1 = {'A':[1,2,3],'B':[4,5,6],'C':[1,1,1]}
df = pd.DataFrame(dict_1)
def sub(a,b):
    return a-b
    
df['D'] =df.apply(lambda x: x['A']+x['B'],axis=1)
df['E'] =df.apply(lambda y: sub(y['A'],y['B']) ,axis=1)
print(df)

#11 DataFrame Columns
df = pd.DataFrame({'A':[1,2,3,4],'B':[9,9,9,9]})
l = df.columns.tolist()
print(l)

#12. Transpose in DataFrame
df = pd.DataFrame({'A':[1,2,3,4],'B':[9,9,9,9]})
print(df)
print(df.T)
print(df.transpose())

#13 loc and iloc in dataframe (where clause)
##loc:
#loc is label-based, which means that we have to 
#specify the name of the rows and columns that we 
#need to filter out.
##iloc:
#On the other hand, iloc is integer index-based. So 
#here, we have to specify rows and columns by their integer index.    

df = pd.DataFrame({'A':[1,2,3,4],'B':[50,60,70,80],
                   'C':[12,19,16,15]})
df['A'] or df.A #both are same

#where condition
df1 = df.loc[df.A > 2] 
df3 = df.loc[df['A'] > 2] 
print(df1,df3)
#multiple
df2 = df.loc[(df.A>2) & (df.B<75)]
print(df2)
#using slicing
print(df,df.loc[1:3],df[0:3])
#only selected columns
print(df.loc[(df.A >2),(['A','C'])])
#update using loc
df.loc[(df.A>2),(['A','C'])] = [8,9]
print(df)

##using iloc
# select rows with indexes
df.iloc[[0,2]]
df.iloc[[0,3]]
df.iloc[[0,3],[1,2]]
#range of rows using iloc
df.iloc[:3]
df.iloc[:2]












