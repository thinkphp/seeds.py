'''
  Computes SQuare RooT in Python SQRT
'''

import math
import sys

class mySQRT:

      #declared N for to compute the sqrt 
      n = -1

      #defined the error, I mean the epsilon eps 
      eps = 0.0001

      #constructor of the class 
      def __init__(self,N,eps=0.0001):
 
          #assign n to self n
          self.n = N

          #assign eps to self eps
          self.eps = eps

      #public method that computes the sqrt
      def solve(self):          

          #initial a0 = n/2
          a0 = n/2
          a1 = (a0 + self.n/a0)/2
       
          while self.fabs(a0,a1) >= self.eps:

                a0 = a1
                a1 = (a0 + self.n/a0) / 2 

          return a0
 
      def fabs(self,a,b):
          
          if a<b:
             return b-a
          else:
             return a-b  

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python sqrt.py N"
      sys.exit()    
   n = float(sys.argv[1])
   print 'SQRT(', n ,')=', math.sqrt(n)
   ob = mySQRT(n)
   print 'SQRT(', n ,')=', ob.solve()