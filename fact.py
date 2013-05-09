#
# Factorial n!
#
import sys

# solution 1 solved iteratively
def fact(n):

    #ensure that n is a natural number 
    if n<0: n = abs(int(n))
    
    #store n! in variable p 
    p = 1
    for i in range(1,n+1):
        p *= i

    #return n!
    return p

def fact2(nr):
    p = 1
    n = nr
    
    while True:
        if n == 1:
           return p
        else:
           p = p * n
           n = n - 1

# solution 2 solved recursively
def fact_rec(n):

    # ensure that n is natural number
    if n < 0: n = abs(int(a)) 
 
    #if n is equal with 1 then return 1 
    if n == 1: 
       return 1
    #otherwise return n(n-1)
    else:
       return n * fact_rec( n - 1 )     

if __name__ == "__main__":
    print len(sys.argv)
    if len(sys.argv) != 2:
        print "Use: python fact.py 20"
        sys.exit()
    n = int(sys.argv[1]) 
    for i in range(1,n):
        print "%s! = %s" % (i, fact(i))