''' 
  Computes the value of e(2.718281827...) using infinite series
  1 + 1/1! + 1/2! + 1/3! + ...
  2 + 1/2! + 1/3!+ ...
'''
import math

def fact(n):
    if n == 0:
       return 1
    else:
       return n*fact(n-1)

def e(EPS):

    v1 = 2
    v2 = v1 + float(1.0/fact(2))
    i = 3 
    while math.fabs(v1-v2) >= EPS:
          v1 = v2
          v2 += float(1.0/fact(i))
          i += 1
    return v2  

print "The mathematical constant e"
print e(0.00000001) #computes the value of e using infinite series
print math.e #mathematical constant e build-in