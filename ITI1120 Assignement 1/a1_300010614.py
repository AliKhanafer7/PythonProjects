#########################################################
# Question 1
#########################################################

def mh2kh(s):
    '''(number)-> number
Converts speed (s) given, from miles per hour to kilometres per hour
Precondition: Speed is a non-negative number'''
    kh= s*1.60934
    return (kh)


#########################################################
# Question 2
#########################################################

import math
def pythagorean_pair(a,b):
    '''(int,int) -> bool
Determines if the values of a and b are a pythagorean pair or not.
Preconditions:None'''
    c=math.sqrt(a**2+b**2)
    return (c==int(c))


#########################################################
# Question 3  
#########################################################
def in_out(xs,ys,side):
    ''' (number,number,number)-> bool
Prints false if coordinate (x,y) is not a query point available in the square described, otherwise, true
Preconditions: Side must be positive'''
    x=float(input("What value do you want to give your x coordinate?"))
    y=float(input("What value do you want to give your y coordinate?"))
    xt=xs+side 
    yt=ys+side 
    print((x,y)>=(xs,ys) and (x,y)<=(xt,yt)) #(xt,yt) define the coordinates to my upper right corner of the square
#########################################################
# Question 4
#########################################################
def safe(n):
    '''(int)->bool
Identifies wether or not a number, n, is a safe number or not. Function will return True if n is safe, if not, False.
Preconditions: n has at most 2 digits and must be a non-negative integer'''
    a= n-9
    b= n//9
    c=n%9
    return(a%10!=0 and b!=10 and c!=0)

#########################################################
# Question 5
#########################################################
def quote_maker(quote,name,year):
    ''' (str,str,int)->str
Returns a sentence that provides information about the, who, when, and what about a certain quote
Preconditions: None'''
    return("In" + " " + str(year) + ", " +"a person called" + " " + name + " " + "said:" + " " + "'"+ quote+"'")
    
#########################################################
# Question 6
#########################################################
def quote_displayer():
    '''(None)->str
Returns a sentence that provides information about the, who, when, and what about a certain quote
Preconditions: None'''
    q1=input("give me a quote:")
    q2=input("who said that?")
    q3=input("What year did he/she say that?")
    print (quote_maker(q1,q2,q3))
#########################################################
# Question 7 
#########################################################
def rps_winner():
    '''(None)->None
Returns wether player 1 won a rock,paper,scissors game vs player 2, or if it was a tie.
Preconditions:None'''
    P1=input("What choice did player 1 make?" + "\n" + "Type one of the following options: rock,paper,scissors:")
    P2=input("What choice did player 2 make?" + "\n" + "Type one of the following options: rock,paper,scissors:")
    print("Player 1 wins. that is" +" " +str( (P1=="rock" and P2=="scissors") or (P1=="paper" and P2=="rock") or (P1=="scissors" and P2=="paper")))
    print("It is a tie.That is not" + " " + str(not P1==P2))
    
#########################################################
# Question 8
#########################################################
import math
def fun(x):
    '''(Number)->float
Finds the value of y of the equation 10^4y=x+3 when user inputs value of x.
Preconditions: x has to be bigger than -3.'''
    y= (math.log10(x+3))/4
    return(y)

#########################################################
# Question 9
#########################################################
def ascii_name_plaque(name):
   '''(string)->None
   Prints rectangle with given name engraved inside.
   Preconditions: None'''
   print("******"+("*"*len(name))+"******")
   print("*"+ "     "+(" "*len(name))+"     "+"*")
   print("*" +"   "+ "__"+ str(name) + "__"+ "   "+"*")
   print("*"+"     "+(" "*len(name))+"     "+"*")
   print("******"+("*"*len(name))+"******")

#########################################################
# Question 10
#########################################################
def draw_bike():
    '''(None)->None
Draws a bike
Preconditions: none'''
    import turtle
    wn=turtle.Screen()
    tt=turtle.Turtle()
    tt.pencolor("black")
    tt.width(5)

    #first wheel
    tt.penup()
    tt.goto(-200,0)
    tt.pendown()
    tt.circle(80)
    tt.penup()
    tt.goto(-200,67)
    tt.pendown()
    tt.color("black","grey")
    tt.begin_fill()
    tt.circle(20)
    tt.end_fill()
    tt.penup()
    tt.goto(-180,90)
    tt.pendown()
    
    # gear
    tt.color("blue")
    tt.width(8)
    tt.goto(-80,50)
    tt.penup()
    tt.goto(-80,30)
    tt.pendown()
    tt.width(2)
    tt.color("black","grey")
    tt.begin_fill()
    tt.circle(20)
    tt.end_fill()
    tt.penup()
    tt.goto(-79,40)
    tt.pendown()
    tt.width(2)
    tt.color("black","white")
    tt.begin_fill()
    tt.circle(10)
    tt.end_fill()

    #pedals and body
    tt.width(8)
    tt.color("black")
    tt.right(95)
    tt.forward(30)
    tt.right(90)
    tt.forward(10)
    tt.right(180)
    tt.forward(20)
    tt.penup()
    tt.goto(-75,60)
    tt.pendown()
    tt.left(85)
    tt.forward(20)
    tt.left(90)
    tt.forward(10)
    tt.right(180)
    tt.forward(20)
    tt.penup()
    tt.goto(-60,60)
    tt.left(60)
    tt.pendown()
    tt.color("blue")
    tt.forward(180)
    tt.left(30)
    tt.forward(30)
    tt.right(90)
    tt.color("red")
    tt.forward(20)
    tt.left(190)
    tt.forward(40)
    tt.penup()
    tt.goto(50,200)
    tt.pendown()
    tt.color("blue")
    tt.forward(200)
    tt.right(65)
    tt.forward(20)
    tt.left(65)
    tt.color("red")
    tt.forward(20)
    tt.right(180)
    tt.forward(40)
    tt.penup()
    tt.left(180)
    tt.forward(25)
    tt.left(120)
    tt.forward(25)
    tt.right(60)
    tt.pendown()
    tt.color("blue")
    tt.forward(100)
    tt.penup()
    tt.goto(-90,72)
    tt.pendown()
    tt.right(125)
    tt.forward(150)
    tt.penup()

    #second wheel
    tt.color("black")
    tt.width(5)
    tt.goto(160,115)
    tt.pendown()
    tt.circle(80)
    tt.penup()
    tt.goto(110,95)
    tt.pendown()
    tt.color("black","grey")
    tt.begin_fill()
    tt.circle(20)
    tt.end_fill()
    tt.penup()
    tt.goto(95,90)
    tt.pendown()
    tt.left(10)
    tt.width(8)
    tt.color("blue")
    tt.forward(60)
    tt.right(25)
    tt.forward(50)
    wn.exitonclick()

    
#########################################################
# Question 11
#########################################################
import math
def alogical(n):
    '''(number)->int
Returns the ammount of times n must be divided by 2 in order to get a number less than or equal to 1
Preconditions: n must be greater than or equal to 1'''
    a=math.log2(n)
    b=math.ceil(a)
    return (b)

#########################################################
# Question 12
#########################################################
def time_format(h,m):
    '''(int,int)->string
Returns time as descriptive string after given the time of day in hours,h, and minutes,m. Minutes are rounded to nearest 5.
Preconditions: h must be an integer between 0 and 23. m must be an integer between 0 and 59.'''
    a=int(5*round(m/5))
    if a==0:
        return (str(h) + " " + "o'clock")
    elif 5<=a<30:
        return (str(a)+" " + "minutes past" + " " + str(h)+ " " + "o'clock")
    elif a==30:
        return ("half past" + " " + str(h)+ " " + "o'clock")
    if h==23:
        if a!=60:
            return (str(60-a) + " " + "minutes to" + " " + str(h-23) + " " + "o'clock")
        else:
            return ("0 o'clock")
    if 35<=a<=55:
        return (str(60-a) + " " + "minutes to" + " " + str(h+1)+ " " + "o'clock")
    elif a>55:
        return (str(h+1) + " " + "o'clock")
    
#########################################################
# Question 13
#########################################################
def cad_cashier(price,payment):
    '''(number,number)->float
Returns real number representing the change a customer should get based on the price and the amount he payed
Preconditions: price and payement must be real non-negative numbers with two decimal places.Payment must be greater or equal to price.'''
    a= (round (price*100/5)*5)/100
    b=round(payment-a,2)
    return b
#########################################################
# Question 14
#########################################################
def min_CAD_coins(price,payment):
    '''(number,number)->Tuple
Returns the smallest number of coins in toonies, loonies, quartars, dimes and nickels a cashier must return to the customer.
Preconditions:price and payement must be real non-negative numbers with two decimal places.Payment must be greater or equal to price.'''
    a=(cad_cashier(price,payment))*100
    b=int(a//200)
    c=a%200
    d=int(c//100)
    e=c%100
    f=int(e//25)
    g=e%25
    h=int(g//10)
    i=round(g%10)
    j=int(i//5)
    return (b,d,f,h,j)
    
    



