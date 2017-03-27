'''
  Display Numbers Primes
  Website     : http://thinkphp.ro
  Google Plus : http://gplus.to/thinkphp
  MIT Style License
'''

import math
import sys

def allPrimes( nr ):

    n = 2
    contor = 0

    out = ''

    while contor != nr:

       prime = True
       start = 2

       to = int( math.sqrt( n ) )

       for i in range(start, to + 1):

          if n % i == 0:
              
              prime = False

              break

       if prime == True:

          out += str( n ) + ' '

          contor +=1

       n += 1

    return out 

if __name__ == "__main__":

   if len(sys.argv) != 2:

      print "Usage: python primes.py 32"
      sys.exit()

   n = int(sys.argv[1])

   print allPrimes(n)


 