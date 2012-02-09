'''
  Sieve of Eratosthenes in Python

  Twitter     : http://twitter.com/thinkphp
  Website     : http://thinkphp.ro
  Google Plus : http://gplus.to/thinkphp
  MIT Style License     
'''
import sys

def erathostene(n):
 
    v = []
    n = int(n)
    out = ''
    for i in range(0,1000):
        v.append(1)

    for j in range(2,n):
        if v[j]:
           k = 2
           while k*j <= n:
                 v[k*j] = 0
                 k += 1 
    
    for l in range(2,n):
        if v[l]:
           out += str(l) + ' '
    return out

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python eratosthene.py 100"
      sys.exit()
   n = int(sys.argv[1])
   print erathostene(n)