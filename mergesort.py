class Mergesort:

      vec = []

      len = -1

      def __init__(self,arr):

          self.vec = arr

          self.len = len(arr)

      def sort(self):

          self._divimp(0,self.len-1)

      def _merge(self,li,m,ls):
          i = li
          j = m+1
          k = li
          b = [0,0,0,0,0,0,0,0,0]
           
          for t in range(li,ls+1):	
              b[t] = self.vec[t]

          #print b 

          while i<=m and j<=ls:

              if b[i]<b[j]:
                 self.vec[k] = b[i]
                 k = k + 1
                 i = i + 1
              else:
                 self.vec[k] = b[j]
                 k = k + 1
                 j = j + 1

          if i<=m:
             for w in range(i,m+1):
                 self.vec[k] = b[w]   
                 k = k + 1

          if j<=ls:
             for w in range(j,ls+1):
                 self.vec[k] = b[w]
                 k = k + 1

      
      #private method using divide and impera style
      def _divimp(self,li,ls):

          if li == ls:
             return

          m = (li+ls)/2
          self._divimp(li,m)
          self._divimp(m+1,ls)
          self._merge(li,m,ls)

      #@public
      #display the array
      def get(self):
          return self.vec 

arr = [9,8,7,6,5,4,3,2,1]
obj = Mergesort(arr)
obj.sort()
print obj.get()
         