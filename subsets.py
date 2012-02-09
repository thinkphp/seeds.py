'''
  Subsets Algorithm
'''
def subsets(n):

    v = []
    out = ''
    for i in range(0,n):
        v.append(0)
    s = 0    

    while s<n:

      v[n-1] += 1
      
      for j in range(n-1,0,-1):
          if v[j] > 1:
             v[j] = 0
             v[j-1] += 1

      for i in range(0,n):
          if v[i]:
             out += str(i+1) + ' '
      out += '\n' 
 
      s = 0
      for k in range(0,n):
          if v[k] == 1:
             s = s + 1
    print out

subsets(3)