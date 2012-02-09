from arrays import Array

class Stack:
      """  
          A well-known data structure
          Array-based stack implementation 
      """

      DEFAULT_CAPACITY = 10 #class variable for all array stacks 

      def __init__(self):

          self._items = Array(Stack.DEFAULT_CAPACITY)
          self._top = -1
          self._size = 0

      def push(self, newItem):

          """ inserts newItem at top of the stack """
          #resize array if necessary
          if len(self) == len(self._items):
             temp = Array(2*len(self)) 
             for i in xrange(len(self)):
                 temp[i] = self._items[i]
             self._items = temp 
          #newItem goes at logical end of array 
          self._top += 1
          self._size += 1
          self._items[self._top] = newItem
          return newItem

      def peek(self):

          """ precondition: the stack is not empty; returns the item at top of the stack """  
          return self._items[self._top]

      def pop(self):     

          """ precondition: the stack is not empty; removes and returns the item at top of the stack """  
          _olditem = self._items[self._top]
          self._size -= 1
          self._top -= 1   

          return _olditem

      def isEmpty(self):

          """ test if the stack is empty or not """  
          return len(self) == 0 

      def __str__(self):

          """ items string from bottom to top """  
          out = ""
          for i in xrange(len(self._items)):
              out += str(self._items[i]) + " "
          return out 

      def __len__(self):

          #returns the number of the items in the stack
          return self._size


     
if __name__ == "__main__":
    st = Stack()
    print 'push: ', st.push(9)
    print 'push: ', st.push(7)
    print 'push: ', st.push(2)
    print 'push: ', st.push(1)
    print 'push: ', st.push(8)

    print len(st)
   
    print 'pop: ',st.pop()
    print 'pop: ',st.pop()
    print 'pop: ',st.pop()
    print 'pop: ',st.pop()
    print 'pop: ',st.pop()
    print st  
    print 'Is empty? ', st.isEmpty()
    print 'Len:', len(st)
