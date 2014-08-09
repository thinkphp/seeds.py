#Binary Search

#iterative solution
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

#recursive solution
def binarySearchRec(what,li,ls,arr):
     
    if li>ls:
       return False
  
    middle = (li+ls)/2

    if what == arr[middle]:
       return middle

    elif what > arr[middle]:

       return binarySearchRec(what,middle+1,ls,arr)

    else:
       return binarySearchRec(what,li,middle-1,arr) 

#I'm using recursively solution as well
def searchbin(arr, x):

    return _searchbin(arr, x, 0, len(arr)-1)

def _searchbin(arr, x, li, ls):

    if li>ls: 
       return -1

    m = (li+ls)/2

    if x == arr[m]:
       return m 

    if x > arr[m]: 
       return _searchbin(arr,x,m+1,ls)

    if x < arr[m]: 
       return _searchbin(arr,x,li,m-1)    


#main
if __name__ == "__main__":

     arr = [1,2,3,4,5,6,7]
     search = 3

     #assert 19 == binarySearch(20,arr)

     #first attempt
     print binarySearch(2,arr)

     #second attempt
     print binarySearchRec(22,0,len(arr)-1,arr)

     #third attempt
     print arr
     print 'I am searching...:', search
     print 'Position:', searchbin(arr,search)


    

