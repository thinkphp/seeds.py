# This is a small class to compute a^b using bitwise based on Exponentiation by Squaring
import math

class Exp:

      def __init__(self, a, b):

          #first number that is named base
          self.a = a

          #second number that is named exponent
          self.b = b

      def solve1(self):
 
          sol = 1

          x = self.a

          y = self.b

          i = 0 

          while (1<<i) <= y:

                 if ( (1<<i) & y) > 0:

                     sol = sol * x

                 x = x * x

                 i = i + 1  

          return sol

      def solve2(self):
 
          sol = 1

          x = self.a

          y = self.b

          while y:

                if y&1:

                   sol = sol * x
                   y -= 1

                x *= x 
                y /= 2  

          return sol

      def solve3(self):
 
          sol = 1

          x = self.a

          y = self.b

          for i in range(0, y):

              if (1<<i)&y:

                  sol = sol * x

              x = x * x
  
          return sol


      def solve4(self):

          sol = 1

          x = self.a

          y = self.b 
 
          c = y

          bin = [ 0 ] * y

          bin[ 0 ] = 0

          while y:

            bin[ 0 ] = bin[ 0 ] + 1

            bin[ bin[ 0 ] ] = y % 2

            y /= 2

          for i in range(1, bin[ 0 ] + 1):

              if bin[i]:

                 sol = sol *x

              x = x * x 

          return sol

ob = Exp(1112,1221)

#print ob.solve1()            
#print ob.solve2()  
#print ob.solve3()  
print ob.solve4()    
                  



