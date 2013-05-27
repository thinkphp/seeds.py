#
# Decomposition in prime factors
# 4!
# 2^3
# 3^1
#
import sys

def factors(n):
    m = []
    for i in range(2,1000):
        m.append(0)

    for xx in range(2,n+1):
        x = xx
        for d in range(2,n+1):
            if x % d == 0:
               while x % d == 0:
                     m[d] += 1 
                     x = x / d
            if x <= 1:
               break   

    for d in range(2,n):
        if m[d]:
           print d , '^' , m[d] 
     
factors(200)