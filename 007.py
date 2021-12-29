# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# prime numbers = prvocisla

#Sieve of Eratosthenes - find all prime numbers to given limit

# Create matrix of given size
def getMatrixGivenLimit(limit):
    matrix = []
    limit_=int(limit)
    for i in range (2,limit_):
        matrix.append(i)
    return matrix


def excludeIteration(matrix, iteration):
    finalMatrix = matrix
    beginningFlag = True

    for i in matrix:
        if (i > iteration) and (not beginningFlag):
            if not i%iteration:
                finalMatrix.remove(i)

        beginningFlag = False
    return finalMatrix

def getElementByIndex(index, matrix):
    if len(matrix) > index:
        return matrix[index-1]
    else:
        print('error, out of range')

def calc():
    rang = 99999
    index = 6
    finalMatrix = getMatrixGivenLimit(rang)

    for i in range (2, rang):
        finalMatrix = excludeIteration(finalMatrix,i)
        
    # print(finalMatrix)

    result = getElementByIndex(index, finalMatrix)
    print(str(result))

calc()