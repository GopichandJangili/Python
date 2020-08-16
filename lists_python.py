#lists : it it a collection
#Features : Indexed, ordered, mutable, allows duplaictes

#Allows different data types 
a = ['a',1,2,'b']
print(a)


s = 'human'
#empty list
a = []
for string in s:
    a.append(string)
print(a)

# Reversing a lit
a = [1,2,3,4]
b = a[::-1]   # using start, end , step
c = list(reversed(a)) #using reversed
print(b)
a.reverse() #using reverse
print(a)

#sorting a list
a = [1,2,3,7,6]
c = a.copy()
a.sort()
print(a)
c.sort(reverse=True)
print(c)

#Deleting a list completely
a = [1,2,3]
print(a)
del a   

#remove
a = [1,2,3,4,5,6]
a.remove(3)
print(a)

#pop
a = [1,2,3,4,5]
b = a.copy()
a.pop()   #removes from last and returns the element
print(a)
b.pop(0)  #removes based on index
print(b)

    
#using list comprehension
a = [x for x in 'human']
print(a)

#slicing in list
l = ['1','2','3','4','5']
print(l[:2],l[-2:],l[-3:-1])

#list of list
l1= [[1,2],[3,4],[5,6]]
print(l1)

#range funciton
x = range(1,5)
print(list(x))

# Minus 
a = [1,2,3]
b = [3,4,5]
print([x for x in a if x not in b])

#appending to lists
a = [1,2,3]
b = [3,4,5,6]
print(a+b)   #extending lists
a.extend(b)
print(a)


#Reversing a list
a = [1,2,3,4]
print(a[::-1])

#Multiple conditions in list comprehension
a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x < 8 if x%2==0]
print(b)

#conversions
#Tuple to list
import numpy as np
a = (1,2,3,4)
print(list(a))
#numpy array to list
ar = np.array([1,2,3])
l = list(ar)
print(l)  
#set to list
a = {1,2,3}
l = list(a)
print(l)

#dataframe column to list
import pandas as pd
df = pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8],'C':[2,3,4,5]})
print(df)
l = df['A'].tolist()
print(l)
s = pd.Series([1,2,3,4])
l1 = list(s)
print(l1)

#Aggregations on lists
l = [1,2,3,4]
print(sum(l),min(l),max(l))

# Delete dupliates
#1
a = [1,2,2,3]
b = list(set(a))
print(b)
c = []
for x in a:
    if x not in c:
        c.append(x)
print(c)

#functions
a = [1,2,3,4]
b = a.copy()  #create another copy of this list
print(b)
c = a.copy()
print(c)
c.clear()  # deletea all data in a list
print(c)


#miltiply all elements of list
l = [1,2,3,4]
x =1
for e in l:
    x = x*e
print(x)

#get largest number in a list
a = [1,2,3,4]
x = a[0]
for e in a:
    if x>e:
        x = a[0]
    else:
        x = e
print(x)

# length >2; first and last characters are same
l = ['abc', 'xyz', 'aba', '1221']
new_lis = []
for s in l:
    if len(s)>2 and s[0]==s[-1]:
        new_lis.append(s)
print(new_lis)


#Adding elements of two lists
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
l3 = [x+y for x,y in zip(l1,l2)]
print(l3)

#sort a list based on last element in the tuple
def last(r):
    return r[-1]

l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
x = sorted(l,key=last)
print(x)


        
#Sorting a list of lists based on last element
def fun(x):
    return x[-1]
  
a = [[1,2],[2,3],[4,5]]
b = sorted(a,key=fun,reverse=True)
print(b)
     
     

        
    
    








