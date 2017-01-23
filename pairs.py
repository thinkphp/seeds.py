import sys

def Pairs(dic, k):

    count = 0
   
    for each in dic:
  
        if each + k in dic:

           count +=1  

    return count

if __name__ == '__main__':

   a = raw_input()
   b = raw_input()  

   firstLine = map(int, a.strip().split(" "))

   _a_size = firstLine[ 0 ]  

   k = firstLine[ 1 ]

   secondLine = map(int, b.strip().split(" "))
  
   myDict = {item: 0 for index, item in enumerate( secondLine )} 

   print Pairs(myDict, k)
 
 