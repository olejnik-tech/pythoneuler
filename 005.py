# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 20

def fce():
    c = 2500 # From which num should I count? (x=10 -> valid=2520)
    valid = False
    while not valid:
        #print('current: ',str(c))
        for i in range(1, x+1):
            valid = True
            #print("counting current ",str(c)," with modulo ",str(i)," result ",str(c%i))
            if c%i != 0:
                valid = False
                break;
        if valid:
            print("VALID: ",str(c))
        else:
            c+=1

fce()
#232792560
