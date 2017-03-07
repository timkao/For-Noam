# The function will find a prime number based on the number you give to it. For example, if your input is 1, the function will retrun 2.
# if your input is 2, the function will return 3.
# if your input is 5, the function will return 11.


def PrimeMover(num): 
	result = []
	n1 = 1
	n2 = 100
	while len(result) < int(num):
		for i in range(n1, n2+1):
			prime = []
			for j in range(1, i +1):
				if i % j == 0:
					prime.append(j)
				else:
					continue
			if len(prime) == 2:
				result.append(i)
			else:
				continue
		n2 += 100
		n1 += 100
	return result[int(num)-1]
