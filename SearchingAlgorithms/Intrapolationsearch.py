'''
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]
Rest of the Interpolation algorithm is same except the above partition logic.
Step1: In a loop, calculate the value of “pos” using the probe position formula.
Step2: If it is a match, return the index of the item, and exit.
Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array. Otherwise calculate the same in the right sub-array.
Step4: Repeat until a match is found or the sub-array reduces to zero.
'''
##Iterative Algorithm
def interpolationSearch(arr, n, x):##arr = array, x = key, n = length of array
    # Find indexs of two corners
    lo = 0
    hi = (n - 1)
  
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Probing the position with keeping
        # uniform distribution in mind.
        pos  = lo + int(((float(hi - lo) /
            ( arr[hi] - arr[lo])) * ( x - arr[lo])))
 
        # Condition of target found
        if arr[pos] == x:
            return pos
  
        # If x is larger, x is in upper part
        if arr[pos] < x:
            lo = pos + 1;
  
        # If x is smaller, x is in lower part
        else:
            hi = pos - 1;
     
    return low-1
	
