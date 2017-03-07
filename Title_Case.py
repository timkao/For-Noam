# turn a string into "Title" style
# however, has the flexibility to say which word should not be captalized

def titleCase(title, minor_words):
	t_list = title.lower().split(" ")
	m_list = minor_words.lower().split(" ")
	listresult = []
	for i in range(0, len(t_list)):
		if i == 0:
			listresult.append(t_list[i].capitalize())
		elif i > 0:
			if t_list[i] in m_list:
				listresult.append(t_list[i])
			else:
				listresult.append(t_list[i].capitalize())
				
	return " ".join(listresult)

print titleCase('THE WIND IN THE WILLOWS', 'The In')
