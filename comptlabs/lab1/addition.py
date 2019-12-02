def addition(a,b):
	asize=len(a)
	bsize=len(b)
	summ=""
	carry=0
	if asize<bsize:
		temp=a
		a=b
		b=temp
	i=min(asize,bsize)-1
	j=max(asize,bsize)-1
	while i>=0:
		c = int(a[j]) +int(b[i])+carry
		carry = c//10
		summ=str (c%10)+summ
		i-=1
		j-=1
	while j>=0:
		c = int(a[j]) +carry
		carry = c//10
		summ=str (c%10)+summ
		j-=1
	
	return summ

print(addition("1235767","321"))