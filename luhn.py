#Luhn Python checksum for credit card validation
import sys

def luhn(n):

    sum = 0

    alt = 0

    i = len(n) - 1

    num = 0
    
    while i >= 0:

       num = int( n[ i ] )

       if alt:

          num = num * 2

          if num > 9:

             num = ( num % 10 ) + 1  

       sum = sum + num 
 
       alt = not alt 

       i -= 1
   
    return sum%10 == 0

if __name__ == "__main__":

     if len(sys.argv) != 2:

        print"Usage: python lyhn.py 121232232"

        sys.exit()  

     n = str(sys.argv[1])  

     if luhn( n ):

        print "VALID"

     else:

        print "INVALID"    



