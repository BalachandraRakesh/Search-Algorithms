
##Iterative Algorithm
def binarysearch_iterative(array,high,low,key):
	while(high >= low):
		mid = low + (high - low)//2 ##cant be a float
		if(array[mid] == key):
			print(mid)
			return
		elif(key > array[mid]):
			low = mid + 1
		elif(key < array[mid]):
			high = mid - 1
	print(low-1) ##if key not in the list return where it can be placed 
	return
##Recursive Algorithm
def binarysearch_recursive(array,high,low,key):
	if (high < low):
		print(low-1)
		return
	mid = low + (high - low)//2
	if(array[mid] == key):
			print(mid)
			return
	elif(key > array[mid]):
			binarysearch_recursive(array,high,mid+1,key)
	elif(key < array[mid]):
		binarysearch_recursive(array,mid-1,low,key)
		
	
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
low = 0
high = len(array)-1
key = 21
binarysearch_iterative(array,high,low,key)
binarysearch_recursive(array,high,low,key)
