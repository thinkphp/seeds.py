# The Maximum Subsequence Sum Problem
# ------------------------------------
# Given (possibly negative) integers a1, a2, a3,...,an find the maximum value of E k=i...j.
# The maximum subsequence sum is defined to be 0 if all the integers are negative.


# For example, given the sequence -2, 11, -4, 13, -5, -2, the maximum subsequence sum is 20: a2 through a4

class MSS:

      #declare an array with no elements
      arr = []

      #declare the length of the vector
      len = 0 

      #init the solution is NIL
      sol = 0

      #best position for subsequence  
      jBest = -1 

      #constructor of the class 
      def __init__(self, arr=0):

          self.read()

          #self.arr = arr  

          self.len = len(self.arr)  

      #This algorithm solves the problem with O(N) linear time complexity using Dynamic Programming
      #best[ i ] = max( a[ i ], a[ i ] + best[ i - 1])
      def solveDynamic(self):

          best = [ 0 ] * self.len 

          best[ 0 ] = self.arr[ 0 ]

          bestSum = 0

          for i in range(1, self.len - 1):

              best[ i ] = self.arr[ i ]
              
              if best[ i - 1 ] + self.arr[ i ] > best[ i ]:

                 best[ i ] = best[ i - 1 ] + self.arr [ i ]
              
              if best[i] > bestSum:

                 bestSum = best[ i ]

          self.sol = bestSum   

      #This algorithm solves the problem in O(N log N) time complexity and it's more efficient than O(N)
      def solveDivideEtImpera(self):

          self.sol = self.divideEtImpera(0, self.len-1)

      def divideEtImpera(self,left,right):

          if left == right: 
             return self.arr[ left ]
  
          center = (left + right) / 2 

          bestL = self.divideEtImpera(left,center)

          bestR = self.divideEtImpera(center+1,right)

          maxSuf = -9999
          maxPre = -9999 

          suf = 0
          for i in range(center,left-1,-1): 
              suf += self.arr[i]
              if suf > maxSuf:
                 maxSuf = suf 

          pre = 0
          for i in range(center+1,right+1): 
              pre += self.arr[i]
              if pre > maxPre:
                 maxPre = pre 
           
    
          return max(bestL,max(bestR, (maxSuf+maxPre))) 

      
      #Another solution that solves the problem in O(N^3) time complexity and it's less useful.
      def solveON3(self):

          N = self.len - 1

          bestSum = 0 

          iBest = -1
          jBest = -1

          for i in range(0, N + 1):

              for j in range(N, -1, -1):

                  sum = 0

                  for k in range(i,j+1):

                      sum += self.arr[k]

                  if sum > bestSum:

                     bestSum = sum
                     iBest = i
                     jBest = j

          self.sol = bestSum
          self.jBest = jbest  

      # This simple algorithm solves the problem with O(N^2) time. 
      # There exists a better algorithm that uses divide et impera approach O(n log n) time.
      # or dynamic programming approach O(N) time.
      def solveON2(self):

          n = self.len - 1
          bestSum = 0
          bestPos = -1
          partSum = 0

          for i in range(0, n+1):

              partSum = 0

              for j in range(i, n+1): 

                  partSum += self.arr[ j ]

                  if partSum > bestSum:

                     bestSum = partSum
                     bestPos = j

          self.sol = bestSum
          self.jBest = bestPos

    
      # Another algorithm that uses Dynamic Programming approach with O(N) time.
      # recurence best[i] = sum[i] - min(sum[j...i]) 
      def solveON1(self):

          n = self.len
          sum = [0]*n

          sum[0] = self.arr[0]
          for i in range(1,n):
              sum[i] = self.arr[i] + sum[i-1] 

          best = [0]*n

          sumBest = -999
 
          min = sum[0]
          for i in range(1,n):
                  
              best[i] = sum[i] - min

              if sum[i] < min: 
                 min = sum[i]
 
              if best[i] > sumBest:
                 sumBest = best[i]
                 jBest = i

          self.sol = sumBest
          self.jBest = jBest
 
      def getMaxLength(self):

          return self.sol

      # Display the subsequence on screen in a file.out
      def displaySubseq(self):

          bestSum = self.sol

          j = self.jBest

          sum = 0

          output = []

          f = open('maxsubseqsum.out','w')

          for i in range(j,-1,-1):

              output.append( self.arr[i] )

              sum += self.arr[i]

              if sum == bestSum:
                     break

          f.write(str( output[::-1] ))

          print output[::-1] 

          f.close()

      def read(self):

          f = open('maxsubseqsum.in','r')

          lines = f.readline()

          lines = int( lines )

          self.arr = [0] * int( lines )

          our_seq = f.readline()  
       
          our_seq = our_seq.split("\n")

          our_seq = our_seq[0].split(" ")

          for i in range(0,lines):
  
              self.arr[i] = int(our_seq[i])

          print 'Load from FILE the following sequence: ', self.arr

          f.close() 

#arr = [-2,11,-4,13,-5,-2]

ob = MSS()
ob.solveON1()
print ob.getMaxLength()
ob.displaySubseq()