# capitalized every word in a string

def letterCapitalize(str):
	A = str.split(" ")
	B = []
	for i in A:
		B.append(i.capitalize())
		
	return " ".join(B)
	
print letterCapitalize(raw_input("> "))
