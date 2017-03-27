import sys
import math

def isPrime( n ):

    if(n == 1): return False

    if(n == 2): return True

    if(n == 3): return True

    for i in range(2, int(math.sqrt(n)) + 1):

        if(n % i == 0): 

           return False

        else:

           return True   

if __name__ == "__main__":

     if len(sys.argv) != 2:

        print"Usage: python prime.py 1001"
        sys.exit()  

     n = int(sys.argv[1])  

     if isPrime(n):

        print "Is Prime"
     else:
        print "Not Prime"    