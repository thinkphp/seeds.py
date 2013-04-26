'''
   Reverse number
   @thinkphp   
   MIT Style License
'''
import sys

def reverse(n):
    s = 0
    x = n
    while x:
          s = s*10 + x%10
          x = int(x/10)
    return s

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python reverse2.py 123"
      sys.exit()
   n = int(sys.argv[1])
   print reverse(n)




