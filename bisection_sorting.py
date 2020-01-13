##binary_search / bisection
##....searching an element in sorted array
import math
def bisection(arr,element):
    start = 0
    stop = len(arr)-1
    while start<=stop:
        mid = (start+stop)//2
        if element > arr[mid]:
            start = mid+1
        elif element < arr[mid]:
            stop = mid-1
        else :
            return f'{element} found at index {mid}'
    return f'{element} not found in list'

def bisection_recursive(arr,element,start,stop):
    mid = (start+stop)//2
    if start>stop:
        return f'{element} not found in list'
    else:
        if arr[mid]==element:
            return f'{element} found at index {mid}'
        elif element>arr[mid]:
            start = mid+1
            return bisection_recursive(arr,element,start,stop)
        else:
            stop = mid-1
            return bisection_recursive(arr,element,start,stop)
# l = [1,2,3,4,5,6,7]
# print(bisection(l,1))
# print(bisection_recursive(l,8,0,len(l)-1))
