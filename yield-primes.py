def isPrime(n):
 k = 2  
 p = 1
 if n == 1 or n == 0:
 	return 0
 if n == 2 or n == 3:
    return 1
 while( (k*k) <= n and p):       
       p = (n%k != 0)
       k += 1       
 return p


def generator_series(limit_inf, limit_sup):
     while(limit_inf <= limit_sup):
    	  if isPrime(limit_inf):
             yield limit_inf 
    	  limit_inf+=1

array = []

for i in generator_series(0,1000):
    array.append(i)

print array;    	  
