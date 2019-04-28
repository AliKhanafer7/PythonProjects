import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    # YOUR CODE GOES HERE
    friends.pop(0)
    b=[]
    list_of_users=[]
    for string in friends:
            if len(string)>3:
                new_string=string.split(' ')
                if int(new_string[0]) not in list_of_users:
                    list_of_users.append(int(new_string[0]))
                if int(new_string[1]) not in list_of_users:
                    list_of_users.append(int(new_string[1]))
            if len(string)==3:
                if int(string[0]) not in list_of_users:
                    list_of_users.append(int(string[0]))
                if int(string[2]) not in list_of_users:
                    list_of_users.append(int(string[2]))
    list_of_users.sort()
    for user in list_of_users:
        a=user
        b=[]
        tpl=(a,b)
        for string in friends:
            if len(string)>3:
                c=string.split(' ')
                if int(c[0])==user:
                    b.append(int(c[1]))
                if int(c[1])==user:
                    b.append(int(c[0]))
            if len(string)==3:
                if int(string[0])==user:
                    b.append(int(string[2]))
                if int(string[2])==user:
                    b.append(int(string[0]))
        network.append(tpl)
    return network


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    list_of_friends=[]
    # YOUR CODE GOES HERE
    for tpl in network:
        if tpl[0]==user1:
            for friend in tpl[1]:
                list_of_friends=list_of_friends + [friend]
        elif tpl[0]==user2:
            for friend in tpl[1]:
                list_of_friends=list_of_friends+[friend]
    for num in list_of_friends:
        if list_of_friends.count(num)==2:
            if common.count(num) != 1:
                common=common+[num]
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    user_friends=[]
    previous_counter=0
    most_common=0
    for tpl in network:
        if tpl[0]==user:
            for friends in tpl[1]:
                user_friends=user_friends + [friends]
    for tpl in network:
        counter=0
        if tpl[0]!=user and user not in tpl[1]:
            for friends in tpl[1]:
                if friends in user_friends:
                    counter=counter+1
            if counter>previous_counter:
                previous_counter=counter
                most_common=tpl[0]
    if most_common!=0:
        return most_common
    else:
        return None
                    
    
def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    accumilator=0
    for tpl in network:
        if len(tpl[1])>=k:
            accumilator=accumilator + 1
    return accumilator
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    maximum=0
    for tpl in network:
        if len(tpl[1])>maximum:
            maximum=len(tpl[1])
    return maximum
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    maximum=maximum_num_friends(network)
    for tpl in network:
        if len(tpl[1])==maximum:
            max_friends.append(tpl[0])
    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    number_of_friends=0
    number_of_users=0
    for tpl in network:
        number_of_friends=number_of_friends + len(tpl[1])
    for tpl in network:
        number_of_users=number_of_users+1
    return number_of_friends/number_of_users
    
    
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    all_users=[]
    for tpl in network:
        all_users.append(tpl[0])
    for tpl in network:
        all_users.remove(tpl[0])
        tpl[1].sort()
        if tpl[1]==all_users:
            return True
        else:
            all_users.append(tpl[0])
            all_users.sort()
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''()->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    list_of_users=[]
    a=True
    for tpl in network:
        list_of_users.append(tpl[0])
    while a:
        try:
            ID=int(input('Enter an integer for a user ID: '))
            a=False
        except ValueError:
            print('That was not an integer. Please try again.')
    
    while ID not in list_of_users:
        try:
            print('That user ID does not exist. Try again.')
            ID=int(input('Enter an integer for a user ID: '))

        except ValueError:
            print('That was not an integer. Please try again.')
            ID=int(input('Enter an integer for a user ID: '))
            

    return ID
    

    
    
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommed the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinaly, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
