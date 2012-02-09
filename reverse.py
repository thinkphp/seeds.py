'''
   Reverse the order of the items in the array.
   @thinkphp   
   MIT Style License
'''
import arrays
arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
def reverse(arr):
    m = len(arr) / 2
    n = len(arr) - 1
    for i in range(m):
        arr[i],arr[n-i] = arr[n-i],arr[i]
    return arr

assert arr[::-1] == reverse(arr)
arr.reverse()
print arr




