#no char
a = 'abcdef'
#three single or double quotes for multiline strings

a = '''hi this is a 
three line string \n'''
b = """ This is a double quote
statement"""
print(a,b)

###slicing
a = 'abcdefgh'
print(a[:2],a[2:3],a[-1],a[:-2],a[-3:-1])

#reverse a string
a = 'abcdef'
print(a[::-1])
print(len(a))

print(reversed(a))

print(''.join(reversed(a)))    # second way to reverse a string

#upper, lower, strip and spaces
print(a.upper())
b = 'abcdABCD'
a = 'abcd'
print(b.upper(),b.lower())
print(b.isupper(),b.islower(),a.isupper(),a.islower())
z = 'abcd ef lm'
x = ' cceb '
v = x.strip()
print(x)
print(v)
print(z.strip(),'\n',x.strip())

#count spaces in a string
a = 'abcd ef xy'
print(a.count(' '))
#or
count =0
for i in a :
    if i.isspace():
        count+=1
print(count)

#convert string to list
a = 'abcd'
b = list(a)
print(b)

#endswith
a = 'This is a sentence.'
print(a.endswith('.'))   #this returns True

## string replacement
a = "this is a car"
z = a.replace('car','bike')
print(z)

##Check if a string exists in another string
if 'car' in 'this is a car':
    print('yes')
else:
    print('no')

#splitting a string
a = 'file.csv.txt'
b = a.split('.')
print(b,b[0],b[2])

#escape character
a = "this is an "imp" string"   #will not work
a = "this is an \"imp\" string"
print(a)

#find location of a character
a = "abcd-efgh"
print(a.find('-'))
print(a.index('-'))



a = 'abcdABCD'
print(a.capitalize())   # first letter capital

##############string formatting##########################
#########################################################
#########################################################
#3 Types

a = 'hi'
b = '123'
print('This is first way %s and %s ' %(a,b))
print('This is first way {} and {} '.format(a,b))
print(f'This is first way {a} and {b}')
print(F'This is first way {a} and {b}')


    
    
    




