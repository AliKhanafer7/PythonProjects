######################
#1a)
######################
def largest_34(a):
    '''(Lst)->Number'''
    accumilator=0  #1
    a.remove(max(a)) # n + n
    a.remove(max(a)) # n + n
    accumilator+=max(a) # 1 + n
    a.remove(max(a)) # n + n
    accumilator += max(a) # 1 + n
    return accumilator # 1
# 8n + 4
# Eliminate the constants
#O(n)

######################
#1b)
######################
def largest_third(a):
    '''(lst)->Number'''
    accumilator=0 #1
    x=len(a)//3 # 2
    for i in range(x): #len(a)//3
        accumilator+= max(a) # n + 1
        a.remove(max(a)) # n + n
    return accumilator # 1
# 5 + 4n
#O(n)

######################
#1c)
######################
def third_at_least(a):
    '''(lst)->Number or None'''
    x=(len(a)//3)+1 #3
    a.sort() #n*log_2(n)
    for num in a: #n 
        if a.count(num)>=x: #n^2 + n
            return num #1
    return None #1
# 3 + n*log_2(n) + n + n^2 + n +1 +1
# 5 + 2n + n*log_2(n) + n^2
#O(n^2)



######################
#1d)
######################
def sum_tri(a,x):
    '''(lst,Number)->bool'''
    a.sort()   #n*log_2(n)
    for i in range(len(a)): #n
        b=i  #n
        e=len(a)-1 #n
        while e>=b: #n^2
            
            if (a[i] + a[b] + a[e])==x: #4
                return True #1
            elif (a[i] + a[b] + a[e])>x: #4
                e-=1 #1
            elif (a[i] + a[b] + a[e])<x: #4
                b+=1 #1
    return False #1

# n*log_2(n) + n^2 + 3n + 16
#O(n^2)
