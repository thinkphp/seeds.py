# Mathematical Expression Evaluator using Binary Tree Data Structure
#
# Consider the expression:
# Input File: E = (1+1)*13+10/2
# 
# eval( E )
#  
# Output File: 1+1)*13+10/2 = 31
# 

import re

def writeToFile( E, res ):

    f = open('output.out','w')
    f.write(E + " = " + str( res ) ) 
    f.close

#Eval PostFix Notation 
def postFixEval(E):     

    stack = []

    operators = {
                 '+': lambda x,y: x+y,
                 '-': lambda x,y: x-y,
                 '*': lambda x,y: x*y,
                 '/': lambda x,y: x/y
                }   

    ch = None

    for i in range(0,len(E)):

        ch = str(E[i])
        
        if re.match('\d',ch):

           stack.append(int(ch))

        elif ch in operators:
   
              x = stack.pop(-1)
              y = stack.pop(-1)

              res = operators[ch](y, x)

              stack.append(res)

    return stack[0]

output = []

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

def traversal( node ):

    if node.left:
       traversal( node.left )

    if node.right:
       traversal( node.right )

    output.append( node.op )


def eval( E ):
    
    n = len(E)

    print E

    j = 0

    p =  [0] * (n) 
    ev = [0] * (n)

    i = 0

    while i < n:

        if E[i]=='(':

           j = j + 10

        elif E[i] == ')':
           j = j - 10

        elif E[i] == '+':

           p[i] = j + 1   
           ev[i] = '+'

        elif E[i] == '-':

           p[i] = j + 1   
           ev[i] = '-'

        elif E[i] == '*':

           p[i] = j + 10
           ev[i] = '*'

        elif E[i] == '/':

           p[i] = j + 10
           ev[i] = '/'

        elif re.match("\d", E[i]):

            p[i] = 1000 

            k = i 
            r = 0
            while k<n and re.match("\d", E[k]):
                  i = k
                  r = r*10 + int(E[k])
                  k = k + 1

            ev[i] = r

        i = i + 1

    p = filter(lambda a: a != 0, p)
    ev = filter(lambda b: b != 0, ev) 

    tree = arb(0, len( p )-1, ev, p)

    postfix = traversal( tree )

    return postFixEval( output )

f = open('infix.in','r')

expr = f.readline()

expr = expr.strip()

result = eval( expr )

print result

writeToFile(expr, result )