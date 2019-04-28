import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    print('Shuffling the deck...')
    random.shuffle(deck)
    print()
def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    discovered[p1-1]=original_board[p1-1]
    discovered[p2-1]=original_board[p2-1]
    print_board(discovered)
    
    

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]
    # YOUR CODE GOES HERE
    l.sort()
    for i in l:
        amount= l.count(i)
        if amount%2==1:
            l[l.index(i)]='*'
            
    for j in l:
        if j=='*':
            playable_board= playable_board + []
        else:
            playable_board=playable_board + [j]
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    
    # YOUR CODE GOES HERE
    accumilator=0
    if l==[]:
        return True
    for i in l:
        if l.count(i)!=2:
            accumilator=accumilator+l.count(i)
    if accumilator>0:
        return False
    else:
        return True
####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE
    stars= []
    guesses=0
    size=len(board)

    for i in range(len(board)):
        stars=stars+['*']

    print_board(stars)
    
    while stars!=board:
        print('\n')
        print('Enter two distinct positions on the board that you want revealed.\ni.e two integers in the range ['+str(1)+','+str(size)+']')
        p1=int(input('Enter position 1: '))
        p2=int(input('Enter position 2: '))

        if p1>=1 and p1<=size and p2>=1 and p2<=size:
            if (stars[p1 - 1] == board[p1 - 1]) or (stars[p2 - 1] == board[p2 - 1]):
                if p1!=p2:
                    print('One or both of your chosen positions has already been paired.\nPlease try again. This guess did not count. Your current number of guesses is ' + str(guesses))
                    
                else:
                    print('One or both of your chosen positions has already been paired.')
                    print('You chose the same positions.')
                    print('Please try again. This guess did not count. Your current number of guesses is ' + str(guesses)+'\n')
            
            elif p1==p2:
                print('You chose the same positions.')
                print('Please try again. This guess did not count. Your current number of guesses is ' + str(guesses)+'\n')
            else:
                print_revealed(stars,p1,p2,board)
                print()
                wait_for_player()
                print('\n'*70)
                if stars!=board:
                    if board[p1-1]==board[p2-1]:
                        print_revealed(stars,p1,p2,board)
                    else:
                        stars[p1-1]='*'
                        stars[p2-1]='*'
                        print_board(stars)
                guesses= guesses + 1
                
        else:
            print('One of both of your chosen positions is out of the given range.')
            print('Please try again. This guess did not count. Your current number of guesses is ' + str(guesses))
                
    print('\n'*70)
    print('Congratulations! You completed the game with ' + str(guesses) + ' guesses. that is ' + str(guesses - size//2) + ' more than the best possible.')
    


#main
    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
def ascii_name_plaque(name):
   '''(string)->None
   Prints rectangle with given name engraved inside.
   Preconditions: None'''
   print("******"+("*"*len(name))+"******")
   print("*"+ "     "+(" "*len(name))+"     "+"*")
   print("*" +"   "+ "__"+ str(name) + "__"+ "   "+"*")
   print("*"+"     "+(" "*len(name))+"     "+"*")
   print("******"+("*"*len(name))+"******")
ascii_name_plaque('Welcome to my Concentration game')
print('\n')
option=int(input('Would you like (enter 1 or 2 to indicate your choice):\n(1) me to generate a rigorous deck of cards for you \n(2) or, would you like me to read a deck from a file?\n'))
while option != 1 and option != 2:
    option= int(input(str(option) + ' is not an existing option. Please try again. Enter 1 or 2 to indicate your choice\n'))

    


# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)
if option== 1:
    print('You chose to have a rigorous deck generated for you \n')
    size=int(input('How many cards do you want to play with? \nEnter an even number between 2 and 52: '))
    while not(2<=size and size<=52) or size%2!=0:
        size=int(input('\nHow many cards do you want to play with? \nEnter an even number between 0 and 52: '))
    board=create_board(size)
    shuffle_deck(board)
    wait_for_player()
    print('\n'*70)
    play_game(board)

# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
#print("You chose to load a deck of cards from a file")
#file=input("Enter the name of the file: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)
if option==2:
    print('You chose to load a deck of cards from a file\n')
    file=input('Enter the name of the file: ')
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    a=is_rigorous(board)
    if a==True:
        ascii_name_plaque('This deck is now playable and rigorous and it has '+str(len(board))+' cards.')
    else:
        ascii_name_plaque('This deck is now playable but not rigorous and it has ' + str(len(board)) + ' cards.')
    wait_for_player()
    print('\n'*70)
    shuffle_deck(board)
    wait_for_player()
    print('\n'*70)
    size=len(board)
    if size==0:
        print('The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye')
    else:
        play_game(board)
