import math

class Complex:

      def __init__( self, a, b ): 

          self.a = a
          self.b = b

      def getModule( self ):

          return math.sqrt( self.a**2 + self.b**2 )

      ''' Returns complex number as a string '''
      def __str__( self ):

          return '(%s + i%s)' % (self.a, self.b)

      def add(self, x, y):

          return Complex(self.a + x, self.b + y) 

      def sub(self, x, y):

          return Complex(self.a - x, self.b - y) 


#input = [[2, 7],[5, 4],[9, 2],[9, 3],[7, 8], [2, 2], [1, 1]]

f = open('complex.in','r')

input = [map(int, line.split(' ')) for line in f]

del input[0]


num = len( input )

complexes = [ Complex( i[ 0 ], i[ 1 ] ) for i in input ]

def swapp(c, a, b):

    c[ a ], c[ b ] = c[ b ], c[ a ] 
     
def sort( c ):
    
    swapped = 1

    for i in range(num - 1, 0, -1):

        swapped = 1

        for j in range(0, i):

            if c[ j ].getModule() > c[ j + 1 ].getModule():

               swapped = 0

               swapp(c, j, j + 1)

        if swapped:

           break   

sort( complexes )

f = open('complex.out','w')

for c in complexes:

    f.write('%s\n' % c)     
    print c