#Name: Ali Khanafer
#Student number: 300010614
#Course code: ITI1120
#Assignement #2
import math

#######################################
#Question 2.1
#######################################
def min_enclosing_rectangle(radius,x,y):
    '''(number,number,number)->(number,number)
Returns the x and y coordinates of the bottom-left corner of the smallest
axis-alligned rectangle enclosing a circle
Preconditions: None'''
    ys=y-radius
    xs=x-radius
    
    if radius<0:
        return None
    else:
        return (xs,ys)


#######################################
#Question 2.2
#######################################
def series_sum():
    '''(None)->number
Returns sumer of 1000 + 1/n**2
Preconditions: n must be a non-negative integer'''
    a=0
    integer=int(input('Please enter a non-negative integer: '))

    if integer<0:
        return None
    else:
        for i in range(1,integer+1):
            a= a + (1/i**2)
        answer=1000+a
        
    return answer

#######################################
#Question 2.3
#######################################
def pell(n):
    '''(int)->int
Returns the nTH pell number in the Pell mathematical sequence.
Preconditions: n must be a positive integer'''
    if n<0:
        return None
    if n== 0:
        return 0
    if n==1:
        return 1
    if n>1:
        value=0
        accumilator=1
        oldNumber=0
        if n>=2:
            for i in range(1,n):
                oldNumber=value + accumilator*2
                value=accumilator
                accumilator=oldNumber
    return accumilator
        
        
#######################################
#Question 2.4
#######################################
def countMembers(s):
    '''(str)->int
Returns the number of extraordinary characters in string s
Preconditions:None'''
    accumilator=0
    for i in s:
        if i in 'efghijFGHIJKLMNOPQRSTUVWX23456!\,':
            accumilator=accumilator+1
    return accumilator

#######################################
#Question 2.5
#######################################
def casual_number(s):
    '''(str)->int
Returns an integer representing a number in s
Preconditions:None'''
    accumilator=''
    a=s.replace(',','').replace('-','')
    if a.isnumeric():
        accumilator=accumilator+a
    else:
        return None
    if '--' in s:
        return None
    elif '-' in s:
        accumilator='-' + accumilator
    return int(accumilator)
#######################################
#Question 2.6
#######################################
def alienNumbers(s):
    '''(str)->int
Returns the integer value represented by string s using alien numbers.
Precondtions: s must only include characters 'Ty!aNU' '''
    accumilator=0
    if 'T' in s:
        a=int('T'.replace('T','1024'))*s.count('T')
        accumilator=accumilator + a
    if 'y' in s:
        b=int('y'.replace('y','598'))*s.count('y')
        accumilator=accumilator + b
    if '!' in s:
        c=int('!'.replace('!','121'))*s.count('!')
        accumilator=accumilator+c
    if 'a' in s:
        d=int('a'.replace('a','42'))*s.count('a')
        accumilator=accumilator+d
    if 'N' in s:
        e=int('N'.replace('N','6'))*s.count('N')
        accumilator=accumilator + e
    if 'U' in s:
        f=int('U'.replace('U','1'))*s.count('U')
        accumilator=accumilator+f
    return accumilator
#######################################
#Question 2.7
#######################################
def alienNumbersAgain(s):
    '''(str)->int
Returns the integer value represented by string s using alien numbers.
Precondtions: s must only include characters 'Ty!aNU' '''
    accumilator=0
    for i in s:
        if i=='T':
            accumilator=accumilator+1024
        if i=='y':
            accumilator=accumilator+598
        if i=='!':
            accumilator=accumilator+121
        if i=='a':
            accumilator=accumilator+42
        if i=='N':
            accumilator=accumilator+6
        if i=='U':
            accumilator=accumilator+1
    return accumilator

#######################################
#Question 2.8
#######################################
def encrypt(s):
    '''(str)->str
Returns an encrypted version of string s
Precondtions:None'''
    a=s[::-1]
    accumilator=''
    if len(a)%2==0:
        for i in range(len(a)//2):
            accumilator=accumilator + (s[-1-i]+s[i])
        return accumilator

    else:
        for i in range((len(a)//2)):
            accumilator=accumilator+(s[-1-i]+s[i])
        return (accumilator + s[len(a)//2])

#######################################
#Question 2.9
#######################################
def oPify(s):
    '''(str)->(str)
Returns a string with the letters o and p inserted between every pair of
consecutive characters of s, as follows.If the first character in the pair is
uppercase, it inserts an uppercase O. If however, it is lowercase, it inserts
the lowercase o. If the second character is uppercase, it inserts an uppercase
P. If however, it is lowercase, it inserts the lowercase p. If at least one of
the character is not a letter in the alphabet, it does not insert anything
between that pair. Finally, if s has one or less characters, the function
returnsthe same string as s.

Preconditions:None'''
    accumilator=''
    x=0
    for i in s:
        if x==len(s)-1:
            accumilator= accumilator + s[-1]
            return accumilator
        if i.isalpha() and i.isupper():
            accumilator=accumilator + i + 'O'
            x=x+1
            if s[s.index(i)+1:s.index(i)+2].isalpha() and s[s.index(i)+1:s.index(i)+2].isupper():
                accumilator=accumilator + 'P'
        if i.isalpha() and i.lower():
            accumilator=accumilator + i + 'o'
            x=x+1
            if s[s.index(i)+1:s.index(i)+2].isalpha() and s[s.index(i)+1:s.index(i)+2].islower():
                accumilator= accumilator + 'p'
        if i.isnumeric():
            accumilator=accumilator+i
        
    return accumilator

#######################################
#Question 2.10
#######################################
def nonrepetitive(s):
    '''(str)->bool
Returns True if s is nonrepetitive and False otherwise.
Precondtions:None'''
    s1=''
    s2=''
    if len(s)%2==0:
        for i in s[len(s)//2:]:
            s1=s1 + i
            for n in (s[:len(s)//2]):
                s2=s2+i
    if s1 in s2:
        return True
    else:
        return False
        
    

