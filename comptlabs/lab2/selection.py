def selection(arr):
	for i in range(0,len(arr)):
		min=i
		for j in range(i+1,len(arr)):
			if arr[min]>arr[j]:
				min=j
		if(min!=i):
			temp=arr[i]
			arr[i]=arr[min]
			arr[min]=temp
	return arr
print(selection([8,4,5,12,3,76]))