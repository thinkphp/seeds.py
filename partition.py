# Generate all the partitions of a set
# M = {1,2,3}
# (1),{2},{3}
# (1),{2,3}
# (2),{1,3}
# (3),{1,2}
# {1,2,3}

import sys

def render(v):

    n = len(v)-1
    s = ""

    for i in range(1,n+1):

      if v[i] != 0:   

        s += "{" + str(i)

        for j in range(i+1,n+1):

            if v[i] == v[j]:
               s += str(j) + ""
               v[j] = 0

        s += "}"

    return s 
 
def partition(n):

  v = []
  sol = []
  for i in range(0,n+1):
      v.append(i)

  print render(v)

  k = n;
 
  while True:

    if v[k] != 1:
       max = 1
       for i in range(2,k):
           if v[i]>max and v[i]<v[k]:
              max = v[i]
       v[k] = max

       for j in range(0,n+1):
           sol.append(v[j]) 

       print render(sol)
       sol = []
 
       k = n 

    else:
       v[k] = k
       k = k - 1

    if k == 1: 
       break

  return sol  

partition(4)



