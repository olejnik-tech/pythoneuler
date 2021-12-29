global denominators
global result


def fce(num):
        resultList = []
        denominators = [3, 5]
        result = 0
	
        for i in range(0,num):
                for d in denominators:
                        if( (i%d==0) and (i not in resultList)):
                                #print("num to add: " + str(i))
                                resultList.append(i)
        return sum(resultList)
	
print(fce(1000))

#233168
