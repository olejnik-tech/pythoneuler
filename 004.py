global biggest

def fce(max):
	# browse whole range
	a = max
	b = max
	biggest = 1
	for ai in range (1,a):
		for bi in range (1,b):
			num = ai * bi
			if(palindromChecker(num) and (num > biggest)):
				biggest = num
				break
	print(str(biggest))

def palindromChecker(num):
	numStr = str(num)
	numStrI = numStr[::-1]
	if(numStr == numStrI):
		return True
	else:
		return False
		
		
#palindromChecker(9009);

fce(999)