# Implementations of the Queue using a Python list
# A queue is a specialized list with a limited number of operations in which items can only be added to one end
# and removed from the other. A queue is also known as first-in, first-out (FIFI) list
class Queue:

      def __init__(self):
          self.q = list() #creates an new empty queue,which is a queue containing no items

      def enqueue(self,item):
          self.q.append(item) #adds the given item in the queue
          return item 
        
      def dequeue(self):
          assert not self.isEmpty(), "cannot dequeue from an empty queue." 
          return self.q.pop(0)   #removes and returns the first item in the queue

      def isEmpty(self):

          return len(self) == 0 #returns True if the queue is empty.

      def __len__(self):
          return len(self.q) #returns number if items currently in the queue

      def __str__(self):
          out = ''
          for i in xrange(len(self.q)):
              out += str(self.q[i]) + " "
          return out 


q = Queue()
print 'enqueue: ',q.enqueue(9)
print 'enqueue: ',q.enqueue(8)
print 'enqueue: ',q.enqueue(7)
print 'enqueue: ',q.enqueue(6)
print 'enqueue: ',q.enqueue(11)
print '--------------'
print 'len(queue):',len(q)
print 'dequeue: ', q.dequeue()
