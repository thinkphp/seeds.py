import merge

l = ([2,4,6,8],[1,3,5,7,9],[11,12,13,14,15,16,17])
i = 1;
ll = l[0] 
while i<len(l):
    ll = merge.merge(ll,l[i])
    i +=1

print ll