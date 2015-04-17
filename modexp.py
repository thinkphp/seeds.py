# Modular Exponentiation


class ModExp:

      def __init__(self, a, b, c):

          #first number that is named base
          self.a = a

          #second number that is named exponent
          self.b = b

          #mod
          self.mod = c 

      def solve1(self):
 
          sol = 1

          x = self.a

          y = self.b

          i = 0 

          while (1<<i) <= y:

                 if ( (1<<i) & y) > 0:

                     sol = ( sol * x ) % self.mod

                 x = (x * x) % self.mod

                 i = i + 1  

          return sol

      def solve2(self):
 
          sol = 1

          x = self.a

          y = self.b

          while y:

                if y&1:

                   sol = (sol * x)% self.mod
                   y -= 1

                x = (x * x) % self.mod
                y /= 2  

          return sol

      def solve3(self):
 
          sol = 1

          x = self.a

          y = self.b

          for i in range(0, y):

              if (1<<i)&y:

                  sol = (sol * x ) % self.mod

              x = (x * x )% self.mod
  
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

                 sol = (sol * x ) % self.mod

              x = (x * x ) % self.mod

          return sol

#ob = ModExp(5471,436,7)
ob = ModExp(21,42,1999999973)

print ob.solve1()            
print ob.solve2()  
print ob.solve3()  
print ob.solve4()    
                  



