global result

def fce():
	fib = [0,1]
	result = []
	
	for i in range(2,4000002):
		current = fib[i-1] + fib[i-2]
		fib.append(current)
		
		if ((current%2 == 0) and (current < 4000000)):
			result.append(current)
			print(str(current))
			
		if(current > 4000002):
			break;
			
	print("-----\nResult:")
	print(result)
	print("Sum:")
	print(str(sum(result)))
	return sum(result)
		
fce()

#4613732
