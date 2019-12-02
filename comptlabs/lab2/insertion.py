def insertion(arr):
	for i in range(0,len(arr)):
		elem = arr[i]
		index=i
		while index>0  and arr[index-1]>elem:
			arr[index]=arr[index-1]
			arr[index-1]=elem
			index-= 1
	return arr
print(insertion([23,4,2,78,1,123]))