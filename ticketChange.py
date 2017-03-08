# make sure if we have enough many to give ticket buyer changes

def tickets(people):
	
	pocket = []
	
	for i in people:
		
		pocket.append(i)
		
		if i == 50:
		
			if 25 not in pocket:
				return "NO"
			else:
				pocket.pop(pocket.index(25))
		
		if i == 100:
		
			if 50 not in pocket:
				
				if pocket.count(25) < 3:
					return "NO"
				else:
					pocket.pop(pocket.index(25))
					pocket.pop(pocket.index(25))
					pocket.pop(pocket.index(25))
			else:

				if 25 not in pocket:
					return "NO"
				else:
					pocket.pop(pocket.index(25))
					pocket.pop(pocket.index(50))
		
	return "YES"
	
print tickets([25,25,25,25,50,100,50])
