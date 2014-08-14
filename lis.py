# Longest Increasing Subsequence Problem

class LIS:
   
   #public members for this class
   arr = []

   len = -1 

   L = []

   output = []

   #the constructor of the class
   def __init__(self, arr=[]):

       if len(arr) == 0:

          self.read() 

       else:

          self.arr = arr

          self.len = len(arr)

          self.L = [0] * self.len

          output = [0] * self.len
          

   def read(self):

       #get a pointer to file
       fp = open('lis.in','r')

       #read first line to store the number of elements
       num = fp.readline()

       #convert it to integer to able to be useful, otherwise is string 
       num = int(num)

       #assign num to self.len 
       self.len = num

       #fill up all components of the array to zero
       self.arr = [0]*num

       #fill up all components of the array to zero
       self.L = [0]*num

       #the same thing for output vector
       output = [0]*num

       #read next line, which is in fact our input vector
       input = fp.readline()

       #split \n
       input = input.split("\n")
        
       #split the space between elements 
       input = input[0].split(" ")

       #store to self.arr that is our member
       for i in range(0,num):
           self.arr[i] = int(input[i])

       #close the connection
       fp.close()

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
       self.output.append( self.arr[posMax] )  

       for i in range(posMax+1,n+1):

           if self.arr[i] >= self.arr[posMax] and self.L[i] == max-1:

              self.output.append( self.arr[i] )  
              print self.arr[i]
              max = max - 1     

   def write(self):
       
       print self.output
       fp = open('lis.out','w')
       fp.write(str(self.output))
       fp.close() 

ob = LIS()
ob.solve()
ob.write()
