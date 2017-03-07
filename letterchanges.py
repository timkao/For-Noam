# just a way to change strings

def letterchanges(str):
	A = []
	result = ""
	for i in str:
		if i == "z":
			A.append("a")
		elif i == "Z":
			A.append(A)
		elif (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
			A.append(chr(ord(i) + 1))
		else:
			A.append(i)
	
	for j in A:
		if j in ["a", "e", "i", "o", "u"]:
			result = result + j.upper()
		else:
			result = result + j
	
	return result
	
print letterchanges(raw_input("> "))
