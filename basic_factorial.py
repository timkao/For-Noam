# Give the fuction a number, the function will return the factorial result.
# for example, if your input is 5, it will return 1x2x3x4x5 = 120

def factorial(num):
	begin = 1
	while num > 0:
		begin = begin * num
		num -= 1
	
	return begin
	
print factorial(int(raw_input()))
