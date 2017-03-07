# tell if the given three numbers could make a triangle or not

def is_triangle(a, b, c):
	if (a + b) > c and (b + c) > a and (a + c) > b:
		return True
	else:
		return False
