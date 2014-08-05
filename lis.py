# Longest Increasing Subsequence in Python

import sys

#my Class
class LIS:
   
   arr = []

   len = -1 

   L = []

   #the constructor of the class
   def __init__(self, vec):

       #search the index of the string that is in fact the name of the file!
       i = vec.index('lis.py')

       #then I can remove it
       del vec[i]        

       self.arr = vec

       self.len = len(vec)

       for i in range(0,self.len):

           self.L.append(0)

   def solve(self):

       self.dynamic()    

       self.road()

   def dynamic(self):

       n = self.len - 1
 
       self.L[n] = 1

       for i in range(n-1,-1,-1):
  
           max = 0

           for j in range(i+1,n+1):
               
               if self.arr[j]>=self.arr[i] and self.L[j]>max:

                  max = self.L[j]

           self.L[i] = 1 + max
 
   def road(self):

       n = self.len - 1

       max = self.L[0]

       posMax = 0
 
       for k in range(1, n+1):

           if self.L[k] > max:
              max, posMax = self.L[k], k

       print self.arr[posMax]  

       for i in range(posMax+1,n+1):

           if self.arr[i] >= self.arr[posMax] and self.L[i] == max-1:

              print self.arr[i]
              max = max - 1     
 

if __name__ == "__main__":

   if len(sys.argv) <= 2:      

      print "Usage: python lis.py 4 1 7 6 7"
      sys.exit()

   ob = LIS(sys.argv) 

   ob.solve()