#Triangle Problem using Dynamic Programming

class Triangle:

      matrix = [[]]

      T = [[]]

      road = [[]]

      def __init__(self):

          f = open('triangle.in','r')

          countLines = int(f.readline())

          self.countLines = countLines
 
          #  [[0],
          #   [0,0],
          #   [0,0,0],
          #   [0,0,0,0],
          #   [0,0,0,0,0]]
          self.matrix = [[0 for j in range(0,i+1)] for i in range(countLines)]

          for i in range(0,countLines):

              line = f.readline()

              line = line.split("\n")

              line = line[0].split(" ");
             
              for j in range(0,i+1):
               
                  self.matrix[i][j] = int(line[j])
  
          #self matrix show like this
          #  [[2],
          #   [3,5],
          #   [6,3,4],
          #   [5,6,1,4],
          #   [1,1,9,3,7]]

          self.T, self.road = [[0 for j in range(0,i+1)] for i in range(countLines)], [[0 for j in range(0,i+1)] for i in range(countLines)]

          #   self.T look like this 
          #  [[0],
          #   [0,0],
          #   [0,0,0],
          #   [0,0,0,0],
          #   [0,0,0,0,0]]

          #   self.road looks like this 
          #  [[0],
          #   [0,0],
          #   [0,0,0],
          #   [0,0,0,0],
          #   [0,0,0,0,0]]


      def solve(self):

          countLines = self.countLines

          #copy the last line from self.matrix into self.T
          for j in range(0,countLines):

              self.T[countLines-1][j] = self.matrix[countLines-1][j]

          for i in range(countLines-2,-1,-1):

              for j in range(0, i+1):

                  if self.matrix[i][j] + self.T[i+1][j] > self.matrix[i][j] + self.T[i+1][j+1]:

                     self.T[i][j] = self.matrix[i][j] + self.T[i+1][j]
                     #store the succesor of the j
                     self.road[i][j] = j

                  else:
                     self.T[i][j] = self.matrix[i][j] + self.T[i+1][j+1]
                     #store the succesor of the j
                     self.road[i][j] = j+1

      def writeSolution(self):

          i = 0
          j = 0 
          solutions = [0]*(self.countLines) 

          while i <= self.countLines -1:
                solutions[i] = self.matrix[i][j]
                j = self.road[i][j]   
                i += 1

          f = open('triangle.out','w')

          for i in range(0, self.countLines):
                for j in range(0,i+1):
                    f.write(str ( self.matrix[ i ][ j ] ) )
                    f.write(" ")
                f.write("\n")  

          f.write("Max Sum Road => ")   
          f.write(str(solutions))

          f.close();

          return solutions                 

ob = Triangle()
ob.solve()
print ob.writeSolution()