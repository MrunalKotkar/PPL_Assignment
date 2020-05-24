#to find harmonic divisor no.
nos = []
count = 0
x = 0
while count < 8:
	x = x + 1
	if len(nos)>10:
		break
	list = []
	for i in range(1, x+1):
		if x%i == 0:
			list.append(i)
	sum=0
	for j in range(len(list)):
		sum=sum+(1/list[j])
	har = len(list)/sum
	if har.is_integer() :
		nos.append(x)
		count = count + 1

print(*nos)
