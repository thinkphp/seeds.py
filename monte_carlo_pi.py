'''
   Monte Carlo simulation to approximate PI.
'''
import math
import random

def PI(repeats = 10**5):

    count = 0

    for _ in range( repeats ):

        x, y = random.random(), random.random()
    
        if((x**2 + y**2) <= 1): 

           count+=1    

    return float (4 * count) / repeats   
    

print 'def  PI: ',  PI()
print 'math.pi: ', math.pi 
    