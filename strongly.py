# Strongly Connected Components
# 
# Decomposition a directed graph into its strongly connected components is a classic application of depth-first search.
#  
# Given a directed graph G = (V, E), a strongly connected component(SCC) of G is a maximal set of vertices C subset of V, 
# such that for all u, v in C, both u P v and v P u; that is, both u and v are reachable from each other. In other words, two 
# vertices of directed graph are in the same component if and only if they are reachable from each other.
# 
# Example
# G = (V, E) where V = {1,2,3,4,5} and E = {(1,2),(2,1),(1,3),(2,3),(3,2),(1,4),(4,5),(5,4)}
# There are in this directed Graph two strongly connected components: 
#
# S1 = (1,2,3) 
#
# S2 = (4,5)
#

class SCC: 

      #matrix of roads
      road = [[]]        

      #if not exists road
      infinit = 88

      #number of nodes  
      nodes = -1

      #to store the visited nodes
      succ = []

      #to store the father of node
      pred = []

      #cost
      cost = 0

      #output
      output = [] 

      #component number
      component_number = -1

      #constructor of the class
      def __init__(self):

          #read the graph from namefile.in
          self.readGraph('strongly.in')

          print self.road

      #this algorithm solves the problem with time running O(N^2)  
      def solve(self):

          self.suc = [ 0 ] * (self.nodes + 1)

          self.prec = [ 0 ] * (self.nodes + 1)

          self.component_number = 1
 
          for i in range(1, self.nodes + 1):

              if self.suc[i] == 0:

                 self.depthFirst1(i)  
                 self.depthFirst2(i)
                 self.component_number += 1

              for j in range(1,self.nodes+1):

                 if self.suc[j] != self.prec[j]:

                    self.suc[j], self.prec[j] = 0, 0
              
      def depthFirst1(self, node):

              self.suc[ node ] = self.component_number
 
              for k in range(1, self.nodes+1):

                  if self.road[ node ][ k ] == 1 and self.suc[ k ] == 0:

                     self.depthFirst1( k )
 

      def depthFirst2(self, node):

              self.prec[ node ] = self.component_number
 
              for k in range(1, self.nodes + 1):

                  if self.road[ k ][ node ] == 1 and self.prec[ k ] == 0:

                     self.depthFirst2( k )     

      def displayComponents(self):

             f = open("strongly.out","w")              

             for num in range(1, self.component_number):

                 fout = "Component nr.{}\n".format(num)

                 print fout

                 f.write(fout)

                 for i in range(1, self.nodes + 1):

                     if self.suc[i] == self.prec[i] == num:

                        print i 

                        f.write(str(i))
                        f.write(" ") 

                 f.write("\n")     

             f.close() 
                    
                         
      
      #public method that reads the graph from an input file                                    
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

          for i in range(0, size):

              component = input[ i ]

              node1 = int(component[ 0 ])

              node2 = int(component[ 2 ])

              self.road[ node1 ][ node2 ] = 1


ob = SCC()

ob.solve()

ob.displayComponents()