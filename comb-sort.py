def default_compare(a, b):

    if a < b:
       return -1
    elif a > b:

       return 1

    return 0

def combsort(arr, compare = default_compare):

    gap = len( arr )
    shrinkFactor = 1.3
    swapped = False

    while gap > 1 or swapped:

          if gap>1:
             gap = int(gap / shrinkFactor)

          swapped = False

          for i in range(len(arr)-gap):

              if(compare( arr[i], arr[i+gap])>0 ):

                 arr[i], arr[i+gap] = arr[i+gap], arr[i]

                 swapped = True 
                     
    return arr

arr = [5,4,3,2,1]

print combsort(arr) 