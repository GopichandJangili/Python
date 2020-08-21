#map
''' 
1. map() function returns a map object(which is an iterator) of the 
results after applying the given function to each item of a given iterable 
(list, tuple etc.)
'''
#1. Example
l = [1,2,3,4]
def fun(x):
    return x*2
    
a = map(fun,l)
print(list(a))

#2. Using Lambda

l = [1,2,3,4]
a = map(lambda x:x*3,l)
print(list(a))
