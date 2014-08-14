# Topological Sort

# my Class
class TopSort:

      k = -1 
  
      #constructor of class
      def __init__(self):

          #the first argument is a string containing the filename
          #the second argument is another string containg a few characters describing 
          #the way in which the file will be used
          #in our case the mode is 'r', because the file will only be read
          f = open('topsort.in','r')

          a = f.readline()
         
          #get the number of the lines describing arches
          n = int(a[0])

          #get the numbers of the Nodes
          m = int(a[2])

          #[0,0,0,0,0,0,0,0,0]
          self.isVisited = [0] * (m+1)  

          #[0,0,0,0,0,0,0,0,0]
          self.stack = [0] * m  

          #[0,0,0,0,0,0,0,0,0]
          self.costs = [0] * (m+1)

          #Matrix = [[],[],[],[],[],[],[],[],[],[],[],[]]
          self.Matrix = [[] for j in range(n)]

          print self.Matrix        

          #read each line and construct the Matrix with Costs 
          self.assign(f,n,m)           

      def assign(self,f,n,m):
 
          for i in range(1,n+1):
              l = f.readline()
              i = int(l[0])
              j = int(l[2])

              self.costs[i] += 1
              self.Matrix[i].append(j)

          f.close()

      def solve(self):
           
          self.DFS(1)  

      def solve2(self):
           
          self.DFS2(1)  

      def DFS(self,node):

          self.isVisited[ node ] = 1 
           
          for i in range(0, self.costs[ node ]):
                
              if self.isVisited[ self.Matrix[ node ][ i ] ] == 0:
                 
                 self.DFS( self.Matrix[ node ][ i ] )

          self.k = self.k + 1

          self.stack[ self.k ] = node 

      def DFS2(self,node):

          self.isVisited[ node ] = 1 

          self.k = self.k + 1

          self.stack[ self.k ] = node 
           
          for i in range(0, self.costs[ node ]):
                
              if self.isVisited[ self.Matrix[ node ][ i ] ] == 0:
                 
                 self.DFS2( self.Matrix[ node ][ i ] )

      def write(self):

          #reverse the solution
          print self.reverse(self.stack)

          #returns a file object and is almost commonly used with two arguments
          #first argument is a string containing the filename
          #the second argument is another string containing a few characters describing the way in which will be used the file 
          f = open('topsort.out','w')

          #writes the contents of string to the file 
          print f.write(str(self.stack))

          #when you're done with a file, call f.close() to close it and free up any system resources taken up
          #by the open file.
          f.close()  

      def write2(self):

          print self.stack

          f = open('topsort.out','w')

          print f.write(str(self.stack))

          f.close()  
             
      def reverse(self,arr):

          i = 0
          j = len(arr)-1
 
          while i<j:

             temp = arr[i]    
             arr[i] = arr[j]   
             arr[j] = temp
             i = i + 1
             j = j - 1 

          return arr 

ob = TopSort()
ob.solve2()
ob.write2()
