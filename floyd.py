# Roy-Floyd Algorithm

class Floyd: 

      #matrix of roads
      road = [[]]        

      #infinity
      infinit = 9999 

      #number of nodes  
      nodes = -1

      #output
      output = []

      path = []

      def __init__(self):

          #read the input Graph from FILE.in (graph.in) 
          self.readGraph('floyd.in')

      def solve(self, start, end):

          self._floyd()

          print "Road from {} to {} ".format(start,end)

          print start

          self.path.append(start) 

          self.findPath(start,end)

          f = open('path.out','w')

          f.write(str(self.path))

          f.close()

      def _floyd(self):

          for k in range(1,self.nodes + 1):

              for i in range(1,self.nodes + 1):

                  for j in range(1,self.nodes + 1):

                      if self.road[ i ][ j ] > self.road[ i ][ k ] + self.road[ k ][ j ]:

                         self.road[ i ][ j ] = self.road[ i ][ k ] + self.road[ k ][ j ]
 

      #Find the shortest path from a start point to end point
      #@param i (integer) start point
      #@param i (integer) endpoint point
      #@return void       
      def findPath(self, i, j):
          
          k = 1

          found = 0
 
          #while k is less or equal with number of nodes and not find
          while k <= self.nodes and not found:

             if i is not k and j is not k:
             
                if self.road[ i ][ j ] == self.road[ i ][ k ] + self.road[ k ][ j ]:

                   self.findPath(i, k)     
   
                   self.findPath(k, j)        

                   found = 1

             k += 1

          if not found:
             print j
             self.path.append(j)

      def readGraph(self, filename):

          counter = 0

          input = []
  
          with open(filename, 'r') as file:

               for a_line in file:

                   counter += 1 
                   
                   if counter == 1:

                      number_of_nodes = int(a_line.rstrip())

                   else:

                      input.append(a_line.rstrip()) 

          size = len( input )

          self.nodes = number_of_nodes

          self.road = [[0 for i in range(0, number_of_nodes + 1)] for j in range(0, number_of_nodes + 1)]

          for i in range(0, self.nodes + 1):

              for j in range(0, self.nodes + 1):

                  if i == j:

                     self.road[i][j] = 0

                  else:

                     self.road[i][j] = self.infinit    

          for i in range(0, size):

              component = input[i]
              node1 = int(component[0])
              node2 = int(component[2])
              cost = int(component[4])  

              self.road[node1][node2] = cost


ob = Floyd()
ob.solve(1,3)