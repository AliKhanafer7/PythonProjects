#Name: Ali Khanafer
#Student number: 300010614
#Course code:ITI1120
#Assignement #2
import math
import random


def primary_school_quiz(flag, n):
    # Your code for primary_school_quiz function goes here (instead of keyword pass)
    # Your code should include dosctrings and the body of the function
    '''(int,int)->int
Based on the type of mathematical problems the user wants, flag, the function will return the amount of answers he got right out of n amount of questions.
Preconditions:Flag has to be integer 0 or 1, n must be a positive integer '''
    accumilator=0
    if flag==0:
        for repeat in range(n):
            a=random.randint(0,10)
            b=random.randint(0,10)
            print('Question',repeat+1,":")
            answer=int(input("What is the result of " +str(a)+"-"+str(b)+"?"))
            if answer==(a-b):
                accumilator=accumilator+1
        return accumilator
    if flag==1:
        for repeat in range(n):
            a=random.randint(0,10)
            b=random.randint(0,10)
            print('Question',repeat+1,":")
            answer=int(input('What is the result of'+str(a)+'^'+str(b)+'?'))
            if answer==a**b:
                accumilator=accumilator+1
        return accumilator
    
        
        
 

        
    
    


def high_school_eqsolver(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''(number,number,number)->none
Prints the quadratic equation using the coefficients, a, b and c inputed by the user then solves for x
Precondtions: a, b and c must be real numbers '''
    if a==0 and b==0 and c==0:
        print('The quadratic equation'+ ' '+str(int(b))+'*x'+' + ' +str(int(c)) + '=0' + '\nis satisfied for all numbers of x')
    elif a==0 and b==0 and c!=0:
        print('The quadratic equation'+ ' '+str(int(b))+'*x'+'+'+str(int(c)) + ' =0' + '\nis satisfied for no number x')
    
    elif ((b**2)-(4*a*c))==0:
        print('The quadratic equation '+str(a)+'*x^2'+' + '+str(b)+'*x' + ' + ' + str(c) + ' =0'+'\nhas only one solution, a real roots:')
        print(((-b)/(2*a)))

    elif a==0 and b!=0 and c!=0:
        print('The linear equation ' + str(b)+'*x'+' + ' + str(c) + '\nhas the following root/solution: '+ str(-c/b))
    elif ((b**2)-(4*a*c))>0:
        print('The quadratic equation '+str(a)+'*x^2'+' + '+str(b)+'*x' + ' + ' + str(c) + '=0'+'\nhas the following real roots:')
        print(str(((-b)+(math.sqrt(b**2-4*a*c)))/(2*a)) + " and " + str(((-b)-(math.sqrt(b**2-4*a*c)))/(2*a)))
    elif (b**2-4*a*c)<0:
        print('The quadratic equation '+str(a)+'*x^2'+' + '+str(b)+'*x' + ' + ' + str(c) + '=0'+'\nhas the following complex roots:')
        print(str((-b)/(2*a)) + ' + ' + ' i '+ str(math.sqrt(abs(b**2-4*a*c))/(2*a)))
        print('and')
        print((str((-b)/(2*a)) + ' - ' + ' i '+ str(math.sqrt(abs(b**2-4*a*c))/(2*a))))
    





# main

# your code for the welcome tmessage goes here
def ascii_name_plaque(name):
   '''(string)->None
   Prints rectangle with given name engraved inside.
   Preconditions: None'''
   print("******"+("*"*len(name))+"******")
   print("*"+ "     "+(" "*len(name))+"     "+"*")
   print("*" +"   "+ "__"+ str(name) + "__"+ "   "+"*")
   print("*"+"     "+(" "*len(name))+"     "+"*")
   print("******"+("*"*len(name))+"******")
ascii_name_plaque('Welcome to my math quiz-generator / equation-solver')

name=input("What is your name? ")
status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    ascii_name_plaque(name+', welcome to my quiz-generator for primary school students')
    flag=int(input(name+" what would you like to practice? Enter\n0 for substraction\n1 for exponentiation\n"))
    if flag==0:
        n=int(input("How many practice questions would you like to do?"))
        print(name+" here are your "+str(n)+" questions:")
        correct=primary_school_quiz(flag,n)
            
    if flag==1:
        n=int(input("How many practice questions would you like to do?"))
        print(name+" here are your "+str(n)+' questions:')
        correct=primary_school_quiz(flag,n)
        
    if ((correct/n)*100)>=((9/10)*100):
        print('Congratulations ' + name +'! You\'ll probably get an A tomorrow. Now go eat your dinner and go to sleep.')
        
    if ((correct/n)*100)>= ((7/10)*100) and ((correct/n)*100)<((9/10)*100):
        print('You did well ' + name +',' + ' but I know you can do better.')
        
    if ((correct/n)*100)<((7/10)*100):
        print('I think you need some more practice ' + name+'.')
    


    

    

elif status=='2':
    ascii_name_plaque('quadratic equation, a*x^2 + b*x + c= 0, solver for ' + name)
    

             
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")


        # your code to handle varous form of "yes" goes here
        question=question.replace(' ','')
        question=question.lower()
        

        if question !='yes':
            flag=False
        else:
            
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            a=float(input('Enter a number for coefficient a: '))
            b=float(input('Enter a number for coefficient b: '))
            c=float(input('Enter a number for coefficient c: '))
            high_school_eqsolver(a,b,c)
            
            
 
else:
    # your code goes here
    print(name+' you are not a target audience for this software.')

print("Good bye "+name+"!")
