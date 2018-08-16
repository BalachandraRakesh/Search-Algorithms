'''
A simple approach is to do linear search, i.e

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
'''
## Iterative Algorithm
array = [1,5,3,67,3,9,56,789,765,12,23,43,65,89]
key = 12
low = 0
high = len(array)-1
def linearsearch_iterative(array,key):
	for i in range(len(array)):
		if (key == array[i]):
			print(i)
def linearsearch_recurive(array,key,high,low):
	if(high < low):
		print("Not Found")
		return
	if(array[low] == key):
		print(low)
		return
	else:
		return linearsearch_recurive(array,key,high,low+1)
linearsearch_iterative(array,key)
linearsearch_recurive(array,key,high,low)
