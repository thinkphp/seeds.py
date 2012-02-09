def binarySearch(what,arr):
    li = 0
    ls = len(arr)-1
    while li<=ls:
          middle = (li+ls)/2
          if(what == arr[middle]):
             return middle
          elif what > arr[middle]:
             li = middle + 1
          else:
             ls = middle - 1    
    return False

def binarySearchRec(what,li,ls,arr):
    middle = (li+ls)/2
    if what == arr[middle]:
       return middle
    elif what > arr[middle]:
       return binarySearchRec(what,middle+1,ls,arr)
    else:
       return binarySearchRec(what,li,middle-1,arr)
    

if __name__ == "__main__":
     arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
     #assert 19 == binarySearch(20,arr)
     print binarySearchRec(1,0,len(arr),arr)