'''
x-x^3/3!+x^5/5!-x^7/7!+..-
'''
import sys
import math

def fact(n):
    if n==0:
       return 1 
    else: 
      return n*fact(n-1) 

def pow(x,y):
    p = 1
    for i in range(1,y+1):
        p *= x
    return p

def abs(x,y):
    if x > y:
       return x-y
    else:
       return y-x 

def sin(x):
    eps = 0.0001
    n = 2  
    v1 = x
    v2 = v1 - pow(x,3)*1.0/fact(3)
    while abs(v1,v2) >= eps:
          v1 = v2
          v2 += pow(-1,n)*pow(x,2*n+1)*1.0/fact(2*n+1) 
          n = n + 1
    return v2

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python sin 5"
      sys.exit()     
   x = float(sys.argv[1])
   print'sin(',x,')=', sin(x)
   print'sin(',x,')=', math.sin(x)