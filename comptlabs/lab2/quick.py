def quicksort(arr):
	if len(arr)>1:
		pivot=arr[len(arr)-1]
		j=-1
		for i in range(0,len(arr)):
			if arr[i]<=pivot:
				j+=1
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
		if j<i:
			temp=arr[i-1]
			arr[i-1]=arr[j+1]
			arr[j+1]=temp
			index=0
		for i in range(0,len(arr)):
			if arr[i]==pivot:
				index=i
				break
			
		left=arr[:index]
		right=arr[index:]
		quicksort(left)
		quicksort(right)
	return arr
print(quicksort([12, 11, 13, 5, 6, 7])) 
print(quicksort([4,3,2,1]))