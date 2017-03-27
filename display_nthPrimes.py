'''
  Problem 7 Project Euler
  Display nthPrimes
  Website     : http://thinkphp.ro
  Google Plus : http://gplus.to/thinkphp
  MIT Style License
'''

import math
import sys

def nthPrimes( nr ):

    n = 2

    contor = 0

    outlist = []

    while contor != nr:

       prime = True

       start = 2

       to = int( math.sqrt( n ) )

       for i in range(start, to + 1):

          if n % i == 0:
              
              prime = False

              break

       if prime == True:

          outlist.append(n)

          contor +=1

       n += 1

    return outlist[-1]

if __name__ == "__main__":

   if len(sys.argv) != 2:

      print "Usage: python display_nthPrimes.py 10001"

      sys.exit()

   n = int( sys.argv[ 1 ] )

   print nthPrimes( n )


 