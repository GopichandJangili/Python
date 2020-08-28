#operators
#1. Arithmetic operators
print(1+2,2-1,2*3,2**3) #a**b means a to the power of b
print(5/2,5//2) #5//2 -> means floor division....output is 2 instead of 2.5
print(5%2,4%2) #->modulo operator or gives reminder 

#2. Relational operators
print(5>2,5<2,5>=2,5<=2,5!=2,5==5)   # <> (this is not allowed in python)

#3. Logical operators  (and or not)
a,b,c,d = True,False,True,False
print(a and b,a and c,b and d)
print(a or b) #True
print(not a) #False
print(not b)  #True


#4. Special Operators
#4.1. Identity Operators  (is ; is not)
a,b,c = 2,3,2
print(a is b,a is c)
print(a is not b, a is not c)

#4.2 Membership operators (in ; not in)
a = [1,2,3]
print(1 in a,8 in a)
print(1 not in a,8 not in a)

#5 Ternary Operator
a = '1' if 2==2 else '5'
b = '1' if 2!=2 else '5'
print(a,b)

#6 Any;All
a = [True,True,False,False]
b = [False,False,False]
c = [True,True,True,True]
d =[]
print(any(a),any(b),any(c),any(d))
print(all(a),all(b),all(c),all(d))   #empty becomes in case of True

########some more concepts
print('abc'*3)  #prints the string 3 times

