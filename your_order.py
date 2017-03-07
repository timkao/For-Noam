# sort a string based on the number in the word
# provide three ways

def order(sentence):
	A = sentence.split(" ")
	o_list = []
	result = A[:]
	count = 0
	for i in A:
		for j in i:
			if j in "123456789":
				result[int(j) -1] = str(A[count])
				count += 1

		
	return " ".join(result)
		


# list.insert(index, obj). if len(list) == 0, it will ignore the index of the first element inserted.
# ord(i) sometimes doesn't work
	
def order2(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)
	
def order3(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
