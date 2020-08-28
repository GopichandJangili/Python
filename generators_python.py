# iter function
# The iter() function returns an iterator object.
a = [1,2,3,4]
a = iter(a)
print(next(a),next(a),next(a))

####### miscellanious ###########
a,b =1,2
print(a)
print(b)
print(a,end=" ")
print(b)
#or
print(a,b)

################################



#when to use yeild 
'''The yield statement suspends function’s execution and sends a value back 
to the caller, but retains enough state to enable function to resume where it 
is left off. When resumed, the function continues execution immediately after 
the last yield run. This allows its code to produce a series of values over time,
 rather than computing them at once and sending them back like a list'''
 
'''
We can call it using either using for loop on generator function
or by using next on the iterable object
''' 
 
 
#example
#1
def simple_yield():
    yield 4
    yield 2#next execution starts here
    yield 6
for i in simple_yield():
    print(i)
    
#2
def simple_yield():
    yield 4
    yield 2#next execution starts here
    yield 6
x = simple_yield()
print(next(x),next(x),next(x))
    
'1 example'   
# A Python program to generate squares from 1 
# to 100 using yield and therefore generator

def suqare():
    i = 1
    while True:
        yield i*i
        i+=1
for a in suqare():
    if a >100:
        break
    print(a)

'2 example'
#generate cubes of numbers  
def generator_test():
    i=1
    while 1==1:
        yield i**3
        i+=1
    

for i in generator_test():
    if i <500:
        print(i)

#######################Generators##########################

'''Generator-Function : A generator-function is defined like a normal function,
 but whenever it needs to generate a value, it does so with the yield keyword 
 rather than return. If the body of a def contains yield, the function automatically
 becomes a generator function.'''
 
'''
***Generator-Object : Generator functions return a generator object***. 
Generator objects are used either by calling the next method on the
 generator object or using the generator object in a “for in” loop''' 
 
#1. example - using for loop on a generator object
def sample_generator():
    i=1
    while 1==1:
        yield i**3
        i+=1
for a in sample_generator():
    if a<200:
        print(a)
    else:
        break
    
#2. using next
def generator_new():
    for i in range(1,10):
        yield i

x = generator_new()
print(next(x))

#################################Excercises############################
#######################################################################
#1.Create an array using generator function that generates 15 integers

import numpy as np
def simple_gen():
    i = 1
    while 1==1:
        yield i
        i+=1

list_1 = []
for x in simple_gen():
    if x <= 15:
        list_1.append(x)
    else:
        break
a = np.array(list_1)
print(a)

#or

a = [1,2,3,4]
a = iter(a)

x = np.fromiter(a,dtype='float32')

import numpy as np
def generate():
    for i in range(1,16):
        yield i

a = np.fromiter(generate(),dtype='int')
print(a)



       
    
    
    
    
    

        
        
 
 
 
 
 
 
