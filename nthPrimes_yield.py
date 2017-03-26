'''
 Adrian Statescu
 Display nthPrime
 Usage python nthPrime 101
 MIT License
'''
import sys

def nthPrime(gen, n):

    for i in range(n-1):

        gen.next()

    return gen.next()

def genPrimes():
    
    yield 2
    yield 3

    n = 3
    while True:
        n += 2  
        if isPrime(n):
           yield n

def isPrime(n):

     if n<=1:
        return False

     elif n == 2:
        return True

     elif n == 3:
        return True

     else:
        d = 3
        while d*d <= n:
               if( n % d == 0):
                   return False
               d += 2        

        return True  

if __name__ == "__main__":

   if len(sys.argv) != 2:

      print "Usage: python nthPrimes_yield.py 10001"

      sys.exit()

   n = int( sys.argv[ 1 ] )

   print nthPrime(genPrimes(), n)