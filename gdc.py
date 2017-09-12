import unittest

def GDCDivision(a,b):

    while b != 0:
          tmp = b
          b = a % b
          a = tmp

    return a  

def GDCDivision2(a,b):

    while b != 0:

          r = a % b
          a = b
          b = r 

    return a  

def GDCSubstraction(a,b):
    
    while a!=b:

       if a > b:

          a = a - b

       else:

          b = b - a

    return a   

def GDCRecursive(a, b):
    
    if b == 0:

       return a

    else:

       return GDCRecursive(b, a % b)

class GDCTest(unittest.TestCase):

      def test_basic(self):

          self.assertEquals(GDCSubstraction(10, 3), 1)  
          self.assertEquals(GDCDivision(10, 3), 1)  
          self.assertEquals(GDCDivision2(10, 3), 1)  
          self.assertEquals(GDCRecursive(10, 3), 1) 
 

if __name__ == '__main__':

   unittest.main()  
    
