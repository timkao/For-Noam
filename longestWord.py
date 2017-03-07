# give the function a string, the function will return the word with the most letters in the string for you.
# in the case that a word has "-" or other signs, those signs will not be considered as a letter.

def longestword(str):
	A = str.split(' ')
	base = 0
	clist = []
	
	for i in A:
		count = 0
		for j in i:
			
			if (ord(j) >= 65 and ord(j) <= 90) or (ord(j) >= 97 and ord(j) <= 122):
				count = count + 1
				
		if count > base:
			base = count
			temp_result = i
			
	for k in temp_result:
		
		if (ord(k) >= 65 and ord(k) <= 90) or (ord(k) >= 97 and ord(k) <= 122):
			clist.append(k)
	
	return ''.join(clist)		
	
	
	
print longestword(raw_input('> '))
