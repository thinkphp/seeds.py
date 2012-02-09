#defines a linked list iterator for the list
class NodeIterator:
      def __init__(self,listHead):
          self._currNode = listHead

      def __iter__(self):
          return self

      def next(self):
          if self._currNode is None:
             raise StopIteration
          else:
             item = self._currNode.info
             self._currNode = self._currNode.next
          return item  

#defines a private storage class for creating list nodes
class Node:
      def __init__(self,info):
          self.info = info #field info
          self.next = None #field linked next

'''
   A singly linked list is a linked list in which each node contains a single link field and allows for a complete
   traversal from a distinctive first node to the last.
   Operations: 1) l = LinkedList()
               2) n = len(l)
               3) x in l
               4) l.add(x)
               5) l.remove(x)
               6) traversal for i in l:
               7) __str__ print l
             
'''
class LinkedList:

      #constructs an empty list 
      def __init__(self):
          self._head = None
          self._size = 0

      #returns the number of items in the list
      def __len__(self):
          return self._size

      def add(self,item):
          newNode = Node(item)
          newNode.next = self._head
          self._head = newNode
          self._size += 1   

          return None

      #removes an instance of the item from the linked list
      def remove(self,what):
          predNode = None
          currNode = self._head

          while currNode is not None and currNode.info != what:
                predNode = currNode
                currNode = currNode.next

          assert currNode is not None, "The item must be in the list"

          self._size -=1
          if currNode == self._head:
             self._head = currNode.next
          else:
             predNode.next = currNode.next
             
          return currNode.info

      #membership test using keyword 'in' 
      def __contains__(self,search):
          currNode = self._head
          while currNode is not None and currNode.info != search:
                currNode = currNode.next

          return currNode is not None

      #returns an iterator for traversing the list of items 
      def __iter__(self):
          return NodeIterator(self._head) 

      #converting the list to a string 
      def __str__(self): 
          out = '[LinkedList: '
          curr = self._head
          while curr != None:
               out += str(curr.info) + " "
               curr = curr.next
          out += ']' 
          return out

      def reverse(self):
          curr, prev = self._head, None
          while curr:
               next, curr.next = curr.next, prev
               prev, curr = curr, next
          self._head = prev
 
l = LinkedList()
l.add(1);         
l.add(2);
l.add(3);
l.add(5);
l.add(7);
l.add(8);
l.add(41);

#l: 41 8 7 5 3 2 1

for i in l:
    print i

if 12 in l:
   print '12 exits'
else:
   print '12 not exist' 

print '-----------'
#print 'delete: ', l.remove(41)
print '-----------'

for i in l:
    print i

print "Length of list:", len(l)
l.reverse()
print l