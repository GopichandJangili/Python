#1. A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#2. RegEx can be used to check if a string contains the specified search pattern

#\   Used to drop the special meaning of character
#    following it (discussed below)
#[]  Represent a character class
#^   Matches the beginning
#$   Matches the end
#.   Matches any character except newline
#?   Matches zero or one occurrence.
#|   Means OR (Matches with any of the characters
#    separated by it.
#*   Any number of occurrences (including 0 occurrences)
#+   One or more occurrences
#{}  Indicate number of occurrences of a preceding RE 
#    to match.
#()  Enclose a group of REs
#\s spaces
#\d digits

#replace
a = 'abcd rain'
b = a.split(' ')
a = a.replace('abcd','hi')
print(a,b)


############################ regular expressions ###############
############################ module : re #######################
import re
#funcitons
#findall() --> gives list; search()-->group(), staart(), end() ; sub()--> replacement; 
#split()-->split a sentence

#sub()
text = 'the rain in spain'
a = re.sub('\s','9',text)
b = re.sub('main','rain',text)
c = re.split(' ',text)
print(a,b,c)

#few examples
#1. ^ starting
a = 'hi this is a string'
b = re.search('^h',a)
c = re.search('^a',a)
print(c)
if b:
    print('matched')
else:
    print('no')

#2. $ Ending
a = 'hi how are you'
b = re.search('you$',a)
if b:
    print('matched')
else:
    print('No Match')

#3.[a-h] this includes all a to h ###### [a,h] this includes only a and h
a = 'hi how are you'
b = re.search('[a-m]',a)  #h
c = re.findall('[a-m]',a) #['h', 'i', 'h', 'a', 'e']
d = re.findall('[a,h]',a)
print(b.group())
print(c)
print(d)

#4. ###### . -> any character except new line
txt = 'hello world'
a = re.findall('he...',txt)
print(a)   #output ['hello']

#5. \d -> digits    
txt = 'there are 100 dollars omn the table'
a = re.findall('\d', txt)
print(a) # ['1','0','0']

#6. \s -> spaces
txt = 'there are more spaces here'
a = re.findall('\s', txt) #find spaces
b = re.sub('\s','9',txt)  #replace spaces 
print(a,b)
 
#7. | either or
txt =  'test this pattern'
b = re.findall('test | this ',txt)
print(b)

#8. * zero or more occurances
txt = 'test this pattern'
b = re.findall('tha*',txt)
print(b)

#9. + one or more occurances
txt = 'test this pattern'
b = re.findall('tha+',txt)
c = re.findall('thi+',txt)
print(b,c)

#10 {} number of occurances
txt = 'test all these sentences'
b = re.findall('a{1}l{2}',txt)
print(b)



#example 1 

text = 'this is a sample text'
match = re.search('sample',text)
print(match)
print(match.group(),match.start(),match.end())

#find all
text = 'this is a sample text and sample is repeated again here'
match = re.findall('sample',text)
print(match)









text = 'This is a school'
x = re.search('^T.*l$',text)
if x:
    print('match')
else:
    print('no')

a = 'abcd'
x = re.search('^a',a)
print(x)


#######################################################################
################################ Exercises ############################
#######################################################################

#1. Write a Python program to check that a string contains only a certain 
#set of characters (in this case a-z, A-Z and 0-9).

txt = 'abcbd1234ABCD'
txt_1 = '*12346'
def check_string(txt):
    a = re.findall('[a-z,A-Z,0-9]',txt)
    print(a)
    if len(a) == len(txt):
        return True
    else:
        return False
x = check_string(txt)
y = check_string(txt_1)
print(x,y)

#2. Write a Python program that matches a string that has an a followed by zero or more b's
txt = 'hi this has abbb as value'
txt1 = 'no'
b,c = re.search('ab*',txt),re.search('ab*',txt1)
if b:
    print('yes')
if c:
    print('y')
if not c:
    print('not c')
    
#3. Write a Python program that matches a string that has an a followed by one or more b's.
txt = 'hi this has abbb as value'
txt1 = 'no'
b,c = re.search('ab+',txt),re.search('ab+',txt1)
if b:
    print('yes')
if c:
    print('y')
if not c:
    print('not c')
    
#4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
txt = 'hi this has abbb as value'
txt1 = 'no'
b,c = re.search('ab{0} | ab{1}',txt),re.search('ab{0} | ab{1}',txt1)
if b:
    print('yes')
if c:
    print('y')
if not c:
    print('not c')
    
######## or using questions mark. Question mark makes preceding txt optional
txt = 'hi how'
txt1 = 'a'
txt2 = 'ab'
txt3 = 'abb'
a = re.search('ab?',txt)
b = re.search('ab?',txt1)
c = re.search('ab?',txt2)
d = re.search('ab?',txt3)
if a :
    print('ay')
if b:
    print('by')
if c:
    print('cy')
if d:
    print('dy')


