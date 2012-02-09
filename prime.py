import sys

def isPrime(n):

    if(n == 2): return True

    for i in range(2,n):
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