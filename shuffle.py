"""
Fisher-Yates Shuffle Algorithm implemented in Python

Reference :
https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
http://www.geeksforgeeks.org/shuffle-a-given-array/

Algorithm:
For all N indices of list, swap the element at a given index i with the element at a random index j, where 0 <= j <= i.
"""

from random import randint

def shuffle(arr):

    """
    Shuffle a list 
    """

    n = len(arr)

    for i in range(0, n):

        r = randint(0,i)

        arr[i],arr[r] = arr[r],arr[i] 
    

if __name__ == '__main__':
   arr = [1,2,3,4,5,6,7,8,9]
   print arr
   shuffle(arr)
   print arr