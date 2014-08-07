# Greatest Common Divisor using Euclid's Algorithm

import sys

#my Class that is called GCD Acronim for Greatest Common Divisor simply!
class GCD:
   
   arr = []

   len = -1 
 
   #the constructor of the class
   def __init__(self):

         a = 2
   
   #using an interative solution with the operator =
   #@public method
   def euclid(self,a,b):

          while b != 0:
                a, b = b, a % b     

          return a
  
   #As I mentioned previously its the same thing iteratively
   #@public method
   def euclid2(self,a,b):

          while b != 0:
                r = a % b
                a = b
                b = r

          return a
 
   #using recursively with a litte trick, don't worry because its simple with and or
   #public method
   def euclid3(self,a,b):
 
       return b and self.euclid3(b, a % b) or a

   #the same thing as previous using recursively but without trick, only classical music
   #public method 
   def euclid4(self,a,b):

       if b == 0: 
           return a
       else: 
           return self.euclid4(b,a % b)

   #now for more elements. I supposed that all element are in an array
   def euclidN(self,arr):

       #search the index of the string that is in fact the name of the file!
       i = arr.index('euclid2.py')

       #then I can remove it
       del arr[i]        

       #make this operation with our operator to have our array in our class
       self.vec = arr

       return self.euclidR(0,len(arr)-1)

   def euclidR(self,li,ls):

       if li == ls: 

          return int(self.vec[li])

       m = (li+ls)/2

       return self.euclid(self.euclidR(li,m), self.euclidR(m+1,ls))

if __name__ == "__main__":

   if len(sys.argv) <= 2:      

      print "Usage: python euclid.py 36 45 or python euclid.py 10 3 3 30"
      sys.exit()

   ob = GCD() 
   print ob.euclidN( sys.argv )