#
# Permutation: 3! = 6; (1 2 3) 
# -> (1 2 3) 
#    (1 3 2) 
#    (2 1 3) 
#    (2 3 1) 
#    (3 1 2) 
#    (3 2 1)
#
from __future__ import print_function

#solution 1 iterative
def perm(n):
  p = []
  for i in range(0,n+1):
      p.append(i)   

  while True:
    for i in range(1,n+1):
        print(p[i], end=' ')  
    print("")
    i = n - 1
    found = 0
    while (not found and i>0):
       if p[i]<p[i+1]:
          found = 1
       else:
          i = i - 1    
    k = n
    while p[i]>p[k]:
          k = k - 1
    aux = p[i]
    p[i] = p[k]
    p[k] = aux  

    for j in range(1,(n-i)/2+1):
        aux = p[i+j]
        p[i+j] = p[n-j+1]
        p[n-j+1] = aux
    if not found: 
       break 

print('Solution 1:')

perm(3)

print('Solution 2:')

p = [0,1,2,3]
n = 3

#solution 2 recursive
def perm_rec(k):

    if k == n + 1:
       for j in range(1,n+1):
           print(p[j],end=' ') 
       print('') 
    else:
       for i in range(k,0,-1):
           aux = p[i]
           p[i] = p[k]
           p[k] = aux 
           perm_rec(k+1)
           aux = p[i]
           p[i] = p[k]
           p[k] = aux 


perm_rec(1)     

