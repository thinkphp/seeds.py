#Infix Notation => PostFix Notation using Binary Tree and PostOrder Traversal.

import re

output = []

#write to file.out
def writeToFile( postfix ):

    fp = open('infix2postfix.out','w')

    strout = ''

    for i in range(0, len(postfix)):

        strout = strout + postfix[i]    

    fp.write(strout)

    fp.close()  


# Node that holds the informations
class Node:

    op = 0

    left = 0

    right = 0

    def __init__(self):
      
        a = 2

# Binary Tree Data Structure
def arb(li, ls, ev, pv):

    min = pv[ls]

    posMin = ls

    for i in range(ls, li-1, -1):

        if pv[i] < min:

           min = pv[i]

           posMin = i

    newNode = Node()

    newNode.op = ev[ posMin ] 

    if li == ls:

       newNode.left, newNode.right = 0, 0

    else:

       newNode.left = arb(li,posMin-1,ev,pv)

       newNode.right = arb(posMin+1,ls,ev,pv)

    return newNode
      
def eval( E ):

    n = len(E)

    j = 0

    p = [0] * n 

    ev = [0] * n
    pv = [0] * n

    for i in range(0, n):

        if E[i]=='(':

           j = j + 10

        elif E[i] == ')':
           j = j - 10

        elif E[i] == '+':

           p[i] = j + 1   

        elif E[i] == '-':

           p[i] = j + 1   

        elif E[i] == '*':

           p[i] = j + 10

        elif E[i] == '/':

           p[i] = j + 10

        else:
 
           p[i] = 1000

    k = 0

    for i in range(0, n):

        if E[i] is not '(' and E[i] is not ')': 

           ev[k] = E[i]
           pv[k] = p[i]

           k += 1 

    print ev
    print pv
    arbos = arb(0, k - 1, ev, pv)

    traversal(arbos)

    return output


#Traversal Binary Tree in Postorder
def traversal(node):

    if node.left:
       traversal(node.left)

    if node.right:
       traversal(node.right)

    output.append(node.op)
 
f = open('infix2postfix.in','r')

expr = f.readline()

expr = expr.strip()

f.close()

postfix = eval( expr )

print postfix

writeToFile( postfix )

