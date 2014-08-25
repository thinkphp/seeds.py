import re

operators = {'+': lambda x,y: x+y,
             '*': lambda x,y: x*y,
             '/': lambda x,y: x/y,
             '-': lambda x,y: x-y}

def postfixeval(str):

    stack = []
    n = len(str)
    ch = None

    for i in range(0,n):

        ch = str[i]

        if re.match('\d',ch):

           stack.append(int(ch))

        elif ch in operators:
       
           a = stack.pop(-1)
           b = stack.pop(-1)
           val = operators[ch](a,b)

           stack.append(val)

    return stack[0]         

print postfixeval("2 3 + 7 * 3 *")
