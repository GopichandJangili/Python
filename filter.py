#filter
'''
1. The filter() method filters the given sequence with the help of a function
 that tests each element in the sequence to be true or not
2. returns an iterator that is already filtered.
 
 '''
 
#Note
'''
NOTE : The returned value from map() (map object) then can be passed to functions
 like list() (to create a list), set() (to create a set) 
'''
 
 
#1. Example using function
def fun(a):
    return a%3==0
l = [1,2,3,4,5,6,7,8,9,10]
y = filter(fun,l)
print(next(y),next(y))
print(list(y))


 
#2. Example using lambda 
a = [1,2,3,4]
filter_result = filter(lambda x :x%2==0,a)
c = list(filter_result)
print(type(c),c)

d = [x for x in a if x%2==0]
print(d)