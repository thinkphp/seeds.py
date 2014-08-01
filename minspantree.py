# Minimum Spanning Tree
#  
# An edge-weighted graph is a graph model where we associate weights or costs with each edge. Such graphs are natural
# models for many applications. In an airline map where edges represent flight routes, these weights might represent 
# distances of fares. In an electric circuit where edges represent wires, two weights might represent the length of the wire,
# its cost, or the time that it takes a signal to propagate through it. Minimizing cost is naturally of interest in such 
# situations. In this section, we consider undirected edge-weighted graph model and examine algorithms for one such problem:
# Minimum Spanning Tree. Given an undirected edge-weighted graph, find the MST

# Recall that a spanning tree of a graph is a connected subgraph with no cycles that includes all the vertices. A minimum
# spanning tree (MST) of an edge-weighted graph is a spanning tree whose weight (the sum of the weights of its edges) is no larger
# than the weight of any other spanning tree.

class MinimumSpanningTree: 

      #matrix of roads
      road = [[]]        

      #if not exists road
      infinit = 88

      #number of nodes  
      nodes = -1

      #to store the visited nodes
      S = []

      #to store the father of node
      T = []

      #cost
      cost = 0

      #output
      output = [] 

      #constructor of the class
      def __init__(self):

          #read the graph from namefile.in
          self.readGraph('minspantree.in')

      #public method that gets the minimum cost spanning tree
      def getCost(self):

          return self.cost
      
      def solution(self, n):

          self.draw(n)
          f = open('minspantree.out','w')
          out = "Minimum cost = " + str(self.cost) + "\n"
          out += "Minimum Spanning Tree from 1 to {} => {}". format(n, str(self.output))
          f.write(out) 
          f.close()
          return self.output
           
     
      def draw(self,node): 

          if self.T[ node ] is not 0:

             self.draw( self.T[ node ] )

          self.output.append(node) 

      #this algorithm solves the problem with time running O(N^2)  
      def solve(self):

          #define an array with n nodes
          self.S = [ 0 ] * (self.nodes + 1)

          #define an array with n nodes
          self.T = [ 0 ] * (self.nodes + 1)

          #start with the first node, if we start with second node, possibly we can get another spanning tree
          r = 1

          #step 1 => I mean the start node is selected and the rest of the nodes is r
          self.S[ r ] = 0

          for i in range(1,self.nodes+1):

              if i is not r:

                 self.S[i] = r

          #step 2

          self.cost = 0 

          #execute of n-1 nodes 
          for i in range(1, self.nodes):
           
              min = self.infinit

              for j in range(1,self.nodes+1):

                  if self.S[ j ] is not 0:

                     if self.road[ self.S[ j ] ][ j ] < min:

                        min = self.road[ self.S[ j ] ][ j ]

                        pos = j

              self.cost += self.road[self.S[pos]][pos]

              self.T[ pos ] = self.S[ pos ]

              self.S[ pos ] = 0

              for k in range(1, self.nodes+1):

                  if self.S[ k ] is not 0:

                     if self.road[self.S[k]][k] > self.road[pos][k]:

                        self.S[ k ] = pos
                         
      
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

          for i in range(0, self.nodes + 1):

              for j in range(0, self.nodes + 1):

                  if i == j:

                     self.road[i][j] = 0

                  else:

                     self.road[i][j] = self.infinit          


          for i in range(0, size):

              component = input[ i ]

              node1 = int(component[ 0 ])

              node2 = int(component[ 2 ])

              cost = int(component[ 4 ])

              self.road[ node1 ][ node2 ], self.road[ node2 ][ node1 ] = cost, cost  


ob = MinimumSpanningTree()

ob.solve()

print "Minimum Cost = ",ob.getCost()

n = 4

print "Give me from 1 to the node {} is {}".format(n, ob.solution(n))
