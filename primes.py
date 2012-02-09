'''
  Primes
  Twitter     : http://twitter.com/thinkphp
  Website     : http://thinkphp.ro
  Google Plus : http://gplus.to/thinkphp
  MIT Style License
'''

import math
import sys

def primes(nr):
    n = 2
    contor = 0
    to = int(math.sqrt(nr))
    out = ''
    start = 2
    while contor != nr:
       prime = True
       for i in range(start,to+1):
          if n%i == 0:
              prime = False
              break

       if prime == True or n == 2:
          out += str(n) + ' '             
          contor +=1
       n +=1
    return out 

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python primes.py 32"
      sys.exit()
   n = int(sys.argv[1])
   print primes(n)

 