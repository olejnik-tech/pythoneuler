import math

global largestPrimeFound
global allPrimes

def fce(max):

		largestPrimeFound = 1
		allPrimes = []
		iteration = int(max / largestPrimeFound)
		
		for current in range(largestPrimeFound,max):
			
			if(max%current==0):
				largestPrimeFound = current
				allPrimes.append(current)
				print("Found and appending: " + str(largestPrimeFound))
			
			result = 1
			for prime in allPrimes:
				result = result * prime
			if(result == max):
				print("result = max = ending")
				break
				
	
fce(600851475143)