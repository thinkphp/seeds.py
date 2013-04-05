#
# Euclid's algorithm => Greatest Common Divisor (36,45) = 9
#
import sys

#solution 1 iterative method
def euclid(a,b):

    while b != 0:
        a, b = b, a % b
    return a     

#solution 2 recursive method
def euclid_rec(a,b):

    if b == 0:
       return a
    else:
       return euclid_rec( b, a % b)

#solution 3 trick method a and b or c => a ? b : c
def euclid_trick(a,b):
    return b and euclid_trick(b,a%b) or a

#solution 4 clasic method iterative
def euclid3(a,b):
    while b!=0:
      c = a % b
      a = b 
      b = c
    return a

if __name__ == "__main__":
   if len(sys.argv) != 3:
      print "Usage: python euclid.py 36 45"
      sys.exit()
   a = int(sys.argv[1])
   b = int(sys.argv[2])   
   print euclid_trick(a,b)