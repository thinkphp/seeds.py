# Product Cartesian 
# A = {1,2}
# B = {1}
# C = {1,2,3}
# A x B = {(1,1,1),(1,1,2),(1,1,3),(2,1,1),(2,1,2),(2,1,3)}

import sys

def writeSol(v):
    s = ""
    for i in range(1,len(v)):
        s = s + str(v[i])
    print s

#iterative
def cartesian(cards):

  v = [0,1,1,1]

  m = len(cards)-1

  while True:

    writeSol(v)
 
    i = m

    while i>=1:

       if v[i] >= cards[i]:

          v[i] = 1    

          i = i - 1 

       else:

          v[i] = v[i] + 1

          i = -2

    if i == 0: 
       break

#recursive

v = [0,0,0,0]

cards = [0,2,1,3]

def product_rec(k):
    
    if k == 4:

       writeSol(v)

    else:

       for i in range(1,cards[k]+1):

           v[k] = i

           product_rec(k+1)
 

#iterative
print "iterative:"
print cartesian([0,2,1,3])
#recursive
print "recursive:"
product_rec(1)
