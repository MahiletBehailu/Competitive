def counting(arr,m):
	count = [0 for i in range(0,m)]
	for i in range(0,len(arr)):
		count[arr[i]]+=1
	j=0
	for i in range(0,m):
		while count[i]!=0:
			arr[j]=i
			count[i]-=1
			j+=1
	return arr
		
print(counting([1,3,5,4,1],10))