'''
   Computes the value of PI using infinite series
   4*(1- 1/3 + 1/5 - 1/7 + 1/9 +...)
'''
import math

def PI():
    v1 = 1
    v2 = v1 - float(1.0 / 3.0)
    sign = 1
    i = 5
    EPS = 0.00001
    while 4*abs(v1-v2) >= EPS:
          v1 = v2
          v2 = v2 + sign*float(1.0/i)
          sign = sign*(-1)
          i += 2
    return 4*v2

print 'def  PI: ',  PI()
print 'math.pi: ', math.pi 
    