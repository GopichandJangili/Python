#lambda
'''
1. In Python, anonymous function means that a function is without a name.
2. As we already know that def keyword is used to define the normal functions 
and the lambda keyword is used to create anonymous functions. 
3. It has the following syntax:  
    lambda arguments : expression  
4. This function can have any number of arguments but only one expression,
   which is evaluated and returned.
    '''
#1. example
x = 'sample string'
y = lambda x : x
print(y(x))

#2. example
x = 'test'
(lambda z : z)(x)

#3. example
x = 10
y = lambda p : p**3
print(y(x))

#4. Add 15 
x = input('Enter the number: ')
y = lambda x : int(x)+15
print(y(x))

#5. multiply 2 numbers passed
x = 10
y = 5
z = lambda x,y : x*y
print(z(x,y))

#6. using in return statement
def func_compute(n):
    return lambda x : n/x

result = func_compute(10)
result(5)

#7 sort list of tuples using lambda
a = [('b',1),('a',2),('d',4),('c',3)]
a.sort(key=lambda x :x[0])
a.sort(key=lambda x :x[1])
print(a)

#8 sort list of dictionaries using lambda
a = [{'a':3,'c':1,'b':2},{'a':5,'c':6,'b':1}]
a.sort(key=lambda x:x['b'])
a.sort(key=lambda x:x['b'],reverse=True)
print(a)
#or
b =  sorted(a,key=lambda x : x['a'])

#10. square and cube every number in a list
a = [1,2,3,4,5,6,7,8,9,10]
l1 = map(lambda x : x**2,a)
l2 = map(lambda x : x**3,a)
print(list(l1),list(l2))

#11. check if a string starts with or endswith a character
a = 'python'
y1 = a.endswith('n')
y2 = a.endswith('o')
x1 = a.startswith('p')
x2 = a.startswith('j')
print(x1,x2,y1,y2)
#same thing using lambda
string = 'python'
string2 = 'java'
a = lambda x : True if x.startswith('p') else False
y = a(string)
yy = a(string2)
print(y,yy)

#12. intersection of two arays using lambda
a = [1,2,3,4]
b = [4,1,5,6]
c = [1,2]
c = filter(lambda x : x in a,c)
print(list(c))

#13. Extract Year, Date, Time, Month
from datetime import date,datetime
today = date.today()
print(today)
now = datetime.now()
print(now)
a = lambda x : x.year
b = lambda x : x.month
c = lambda x : x.day
d = lambda x : x.time()
print(a(now),b(now),c(now),d(now))

#replace funciton
a = '1.2.3'
b = a.replace('.','')
c = a.replace('.','',1)
print(b,c)

# Check Digit, alphabet, alphanumeric
a = '1234'
c = 'abcd'
d = '123ancd'
print(a.isdigit())
print(c.isdigit(),c.isalpha())
print(d.isalnum())














