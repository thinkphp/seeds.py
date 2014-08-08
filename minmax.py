# Class MinMax computing for several elements

import sys

#my Class
class MinMax:
   
   arr = []

   len = -1 

   min = 99999

   max = 0
 
   #the constructor of the class
   def __init__(self, vec):

       #search the index of the string that is in fact the name of the file!
       i = vec.index('minmax.py')

       #then I can remove it
       del vec[i]        

       self.arr = vec

       self.len = len(vec)

       self.doMin()

       self.doMax()

   def min(self,a,b):

       if a < b:
          return a
       else:
          return b

   def max(self,a,b):

       if a > b:
          return a
       else:
          return b

   def doMin(self):

       self.min = self.minX(0,self.len-1)

   def doMax(self):

       self.max = self.maxX(0,self.len-1)

   def minX(self,li,ls):

       if li == ls:
          return int(self.arr[li])

       m = (li+ls)/2

       return self.min(self.minX(li,m),self.minX(m+1,ls))

   def maxX(self,li,ls):

       if li == ls:
          return int(self.arr[li])

       m = (li+ls)/2

       return self.max(self.maxX(li,m),self.maxX(m+1,ls))

   def getMin(self):
       
       return self.min       

   def getMax(self):
       
       return self.max

if __name__ == "__main__":

   if len(sys.argv) <= 2:      

      print "Usage: python min.py 36 45 -1 0 1 2 3 4 5"
      sys.exit()

   ob = MinMax(sys.argv) 

   print 'Min = ', ob.getMin()

   print 'Max = ', ob.getMax()