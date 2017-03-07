# identify if the given number is a perfect square number
# if not, return -1
# if yes, return next perfect square

def findpsquare(num):
	A = 1
	B = []
	while num/A >= A:
		if num % A == 0:
			B.append(num/A)
			B.append(A)
		
		A += 1
	
	for i in B:
		if B.count(i) == 2:
			return (i + 1)**2
	
	if num == 0:
		return 1
	
	return -1
	
print findpsquare(int(raw_input("> ")))
