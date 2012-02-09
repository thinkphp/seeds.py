'''
  Implementation of Breadth-First Traversal Algorithm (BFT)
  Given a tree (binary tree), prints all it's elements by level (breadth first traversal)

           9
       2        4

    1    3   5     7

  output would be ->
  9
  2 4
  1 3 5 7
'''

from collections import deque

class Node:

       def __init__(self,info):

           self.info = info
           self.left = None
           self.right = None
           self.level = None

       def __str__(self):

           return str(self.info)


def BFT(node):

    node.level = 1
    queue = deque([node])
    output = []
    current_level = node.level

    while len(queue)>0:

          current_node = queue.popleft()

          if(current_node.level > current_level):
              output.append("\n")
              current_level += 1

          output.append(str(current_node))

          if current_node.left != None:
             current_node.left.level = current_level + 1 
             queue.append(current_node.left) 

          if current_node.right != None:
             current_node.right.level = current_level + 1 
             queue.append(current_node.right)

                 
 
    return ''.join(output)

root = Node(9)
root.left = Node(2)
root.right = Node(4)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(5)
root.right.right = Node(7)

print BFT(root)
     