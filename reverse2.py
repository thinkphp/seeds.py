'''
   Reverse number
   @thinkphp   
   MIT Style License
'''
import sys

#iterative version
def reverse(n):
    s = 0
    x = n
    while x:
          s = s*10 + x%10
          x = int(x/10)
    return s

#recursive solution
def reverse_rec(s,n):
    if n == 0: 
       return s
    else:
       return reverse_rec(s*10+n%10,int(n/10))  

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print "Usage: python reverse2.py 12345678"
      sys.exit()
   n = int(sys.argv[1])
   print reverse_rec(0,n)




