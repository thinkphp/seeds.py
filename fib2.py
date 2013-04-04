#
# Display Fibonacci sequence with start and end using Generators
#

def fib():
    a,b = 0,1
    yield a
    yield b
    while True:
          a, b = b,a + b
          yield b

def display(startSeq,endSeq):
    for cur in fib():
        if cur > endSeq: return
        if cur >= startSeq:
           yield cur

for i in display(0,100):
    print i   

#http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python?rq=1#
