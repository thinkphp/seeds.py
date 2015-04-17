def dec_to_bin(x):

    return int(bin(x)[2:])

f = open('bin.out','w')

num = 8234234324

cnt = 0

for i in range(0, 64):

    if num & (1<<i):
 
       cnt += 1 

print cnt
f.write('%d\n' % cnt) 
f.write('%d' % dec_to_bin( num )) 

f.close()


