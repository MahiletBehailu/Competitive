def multiplication(a):
	anssign=""
	num1=""
	num2=""
	num1sign="+"
	num2sign="+"
	product=""
	d=a.split("*")
	num1=d[0]
	num2=d[1]
	if(num1.startswith("-")):
		num1=num1[1:]
		num1sign="-"
	if(num2.startswith("-")):
		num2=num2[1:]
		num2sign="-"
	if((num1sign=="-" and num2sign=="+") or(num2sign=="-" and num1sign=="+")):
		anssign="-"
	product=multiply(num1,num2)
	if(product!="0"):
		product=anssign+product
	return product

def multiply(a,b):
	asize=len(a)
	bsize=len(b)
	partial=""
	summ=""
	product="0"
	if asize<bsize:
		temp=a
		a=b
		b=temp
	asize=len(a)
	bsize=len(b)
	i=bsize-1
	while i>=0:
		j=asize-1
		carry=0
		summ=""
		while j>=0:
			c=int(b[i])*int(a[j])+carry
			carry = c//10
			summ=str (c%10)+summ
			j-=1
		if(carry!=0):
			summ=str(carry)+summ
		partial=partial+","+summ
		i-=1

	if(partial.startswith(",")):
		partial=partial[1:]
	partarray=partial.split(",")
	
	j=1
	for i in range(0,len(partarray)):
		product=str(int(partarray[i])*j+int(product))
		j*=10
	return product

print(multiplication("1234*-4231"))

		
			
