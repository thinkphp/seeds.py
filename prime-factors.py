#
# Decomposition in prime factors
# 10 = 2^2 * 5^2
#

import sys

def factors(n):

    i = 2 

    while True:
 
      c = 0

      while n % i == 0:
            c = c + 1
            n = n / i

      if c != 0:
         print i, '^', c
     
      i = i + 1

      if n == 1:
         break    


if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python factors 32"
      sys.exit()
   n = int(sys.argv[1])
   factors(n)     