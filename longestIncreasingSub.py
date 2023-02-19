def lis():

    arr = [180,505,30,31,3,75,78,-2]
    n = len(arr)
    best = [0] * (n+1)
    print(arr)
    best[n-1] = 1

    #compute best array for length
    for i in range(n-2, -1, -1):
        temp = arr[i]
        max = 0
        for j in range(i+1, n):
            if arr[j] > temp and best[j] > max:
                max = best[j]
        best[i] =  1 + max
    print(best)
    maxEl = best[0]
    maxPos = 0
    for k in range(1, n):
        if best[k] > maxEl:
            maxEl = best[k]
            maxPos = k
    print(arr[maxPos], end = " ")
    for i in range(maxPos+1, n):
        if arr[i] > arr[maxPos] and best[i] == maxEl-1:
            print(arr[i], end = " ")
            maxEl-=1
lis()
