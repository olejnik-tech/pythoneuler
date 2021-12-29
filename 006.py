# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

global x
x = 100

def fce():
    sumSq1 = 0
    for i in range (1,x+1):
        sumSq1 += i*i
        
    sumSq2 = 0
    for i in range (1,x+1):
        sumSq2 += i
    sumSq2 = sumSq2*sumSq2

    print("RESULT:",str(sumSq2-sumSq1))
        
fce()

#25164150
