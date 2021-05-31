inlinePrimeNumber = ', '.join([str(x[0]) for x in [[x for x in range(2,y-1) if y%x==0] for y in range(0,1000)] if len(x) == 1])
print("Primer Numbers : "+inlinePrimeNumber)
x = 0
while True:
	x+=1
	t = True
	for y in range(2,x-1):
		if x%y == 0: t = False
	if x==1: t = False
	if t : print("Prime number : "+str(x))
