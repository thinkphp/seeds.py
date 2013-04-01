'''
Convert a number from base 10 to base 2
'''
import sys

def tobin(n):
    out = ''
    for i in range(16,-1,-1):
        out = out + str((n>>i)&1)
    return out

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python 10to2.py 100"
      sys.exit()     
   x = int(sys.argv[1])
   print x, '(base 10) => ', tobin(x), '(base 2)'