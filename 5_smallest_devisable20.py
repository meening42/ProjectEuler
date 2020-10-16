# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?
import math

##def isPrime(number):
##    n = int(math.sqrt(number))+1
##    for i in range(2,n):
##        if number%i == 0:
##            return False
##    return True    
##
##def primeFactors(number):
##    reminder = number
##    primes =[]
##    i =2
##    while reminder>1:
##
##        if reminder%i == 0:
##           reminder = reminder/i
##           primes.append(i)
##           i = i-1
##        i = i+1  
##    return primes




def bruteForce(maxDel):
    number = 0
    pogoj = False
    numOfDel = 0
    delitelji = list
    step = maxDel * (maxDel-1)
    while pogoj == False:
        number = number+step
        numOfDel = 0
        for i in range(1,maxDel+1):
            if number%i != 0:
                # print(str(number) +' % '+ str(i)+ '!= 0   ')
                break
            else:
                numOfDel = numOfDel + 1
                # print (str(number) +' % ' +str(i)+ '== 0   ')
        # print numOfDel
        # print number
        if numOfDel == maxDel:
            pogoj = True
            print('This is your special number')
    print(number)

bruteForce(20)

    
    
        
