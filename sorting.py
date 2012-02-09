#Sorting techniques
#Sorting a set with respect to some ordering is a very frequently occuring problem. IBM estimates
#that about 25% of total computing time is spent on sorting in commercial computing centers. The most
#important applications of sorting are(according of Knuth):
# a)collecting related things

class Sorting:

      #define public array
      arr = []
      k = 0

      #constructor of class  
      def __init__(self,arr):

          #self array is assigned
          self.arr = arr

          #get the length of the array
          self.n = len(arr)  

      #sorting by exchanging
      def bubblesort(self): 
              n = self.n
              j = n - 1
              while j >= 0: 
                 for i in range(0,j):
                     if(self.arr[i] >= self.arr[i+1]):
                        self.swap(i,i+1)
                 j=j-1

              return self.arr

      #introduce swap method
      def swap(self,i,j):
          aux = self.arr[i]
          self.arr[i] = self.arr[j]
          self.arr[j] = aux

      #sorting by selection min
      def selectbymin(self):
          n = self.n
          for i in range(0,n):
              k = i
              for j in range(i+1,n):
                    if(self.arr[j] < self.arr[k]):
                       k = j
              if(k != i):
                 self.swap(i,k)

          return self.arr

      #sorting quick sort A.R. Hoare
      def quicksort(self):

          n = len(self.arr)

          self.quick(0,n-1)

          return self.arr

      def quick(self,li,ls):

          if li<ls:
             self.pos(li,ls)
             self.quick(li,self.k-1)
             self.quick(self.k+1,ls)

      def pos(self,li,ls):
              i = li
              j = ls
              i1 = 0
              j1 = -1

              while i < j: 
                if self.arr[i] >= self.arr[j]:
                   aux = self.arr[i]
                   self.arr[i] = self.arr[j]
                   self.arr[j] = aux

                   aux = i1
                   i1 = -j1
                   j1 = -aux

                i = i + i1
                j = j + j1

                self.k = li

      #sorting by merge John von Neumann
      def mergesort(self): 

          n = self.n

          self.divimp(0,n-1)

          return self.arr  

      def divimp(self,li,ls):

          if ls-li <= 1:
             self.sortone(li,ls)
          else:
             middle = (li+ls)/2
             self.divimp(li,middle)
             self.divimp(middle+1,ls)
             self.merge(li,middle,ls)


      def sortone(self,li,ls):

          if self.arr[li] > self.arr[ls]:
             aux = self.arr[li]
             self.arr[li] = self.arr[ls]
             self.arr[ls] = aux

      def merge(self,li,m,ls): 

          i = li
          j = m+1
          c = []
    
          while i<=m and j<=ls:

                if self.arr[i] < self.arr[j]:
                   c.append(self.arr[i])
                   i += 1
                else:
                   c.append(self.arr[j])
                   j += 1 

          if i<=m:
             for x in range(i,m+1):
                 c.append(self.arr[x])
          else:
             for y in range(j,ls+1):
                 c.append(self.arr[y])

          k = 0
          for i in range(li,ls+1):
              self.arr[i] = c[k]
              k +=1
 
arr = [9,8,7,6,5,4,3,2,1,0,-1,123]
ob = Sorting(arr)
print ob.mergesort()
