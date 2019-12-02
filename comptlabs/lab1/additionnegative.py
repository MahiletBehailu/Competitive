
def add(a):
	anssign=""
	num1=""
	num2=""
	num1sign="+"
	num2sign="+"
	sum=0
	if a.startswith("-"):
		num1sign="-"
		a=a[1:]
	d=a.split("-")
	e=a.split("+")
	if len(d)>1:
		num2sign="-"
		num1=d[0]
		num2=d[1]
	elif len(e)>1:
		num1=e[0]
		num2=e[1]
	
	if num1sign=="-" and num2sign=="-":
		anssign="-"
		sum=anssign+addition(num1,num2)
	elif num1sign=="+" and num2sign=="+":
		sum=addition(num1,num2)
	elif num1sign=="-" or num2sign=="-":
		asize=len(num1)
		bsize=len(num2)
		if asize<bsize:
			temp=num1
			num1=num2
			num2=temp
			if num2sign=="-":
				anssign="-"
		elif asize==bsize:
			for i in range(0,asize):
				if(num2[i]>num1[i]):
					temp=num1
					num1=num2
					num2=temp
					if num2sign=="-":
						anssign="-"
					break
			if asize==1:
				if num2[0]>num1[0]:
					temp=num1
					num1=num2
					num2=num1
					if num2sign=="-":
						anssign="-"
				else:
					if num1sign=="-":
						anssign="-"
		if asize>bsize:
			if num1sign=="-":
				anssign="-"
		sum=anssign+diffrence(num1,num2)

	return sum
def diffrence(a,b):
	i=len(b)-1
	j=len(a)-1
	sum=""
	borrow=0
	while i>=0:
		if a[j]>b[i]:
			c=int(a[j])-int(b[i])-borrow
			sum=str(c)+sum
			borrow=0
		elif a[j]<b[i]:
			c=(10+int(a[j]))-int(b[i])-borrow
			sum=str (c)+sum
			borrow=1
		elif a[j]==b[i]:
			c=0-borrow
			borrow=0
			sum=str(c)+sum
		i-=1
		j-=1
	while j>=0:
		c = int(a[j]) -borrow
		if(c!=0):
			sum=str (c)+sum
		j-=1
	while sum.startswith("0"):
		sum=sum[1:]
	if sum=="":
		sum="0"
	return sum
def addition(a,b):
	asize=len(a)
	bsize=len(b)
	sum=""
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
		sum=str (c%10)+sum
		i-=1
		j-=1
	while j>=0:
		c = int(a[j]) +carry
		carry = c//10
		sum=str (c%10)+sum
		j-=1
	
	return sum

#print(addition("1235767","321"))
#print(diffrence("0","1"))
print(add("123+1256783"))