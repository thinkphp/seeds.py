class Array(object):

      def __init__(self,capacity,fill = None):
          """
             capacity is the static size of the array.
             fillvalue is placed at each position  
          """            
          self._items = list()
          for i in xrange(capacity):
              self._items.append(fill)

      def __len__(self):

          return len(self._items)   

      def __str__(self):

          return str(self._items)   

      def __inter__(self):

          return inter(self._items)  

      def __getitem__(self,index):

          return self._items[index]  

      def __setitem__(self,index,newval):

          self._items[index] = newval  

if __name__ == "__main__":
 arr = Array(10)
 print arr

 for i in xrange(len(arr)):
    arr[i] = i + 2
 print arr

 for j in arr:
    print j

