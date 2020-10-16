import math


def isPrime(number):
    if(number <0):
        return False
    if(number == 0):
        return False
    if(number == 1):
        return False
    if(number == 2):
        return True
    n = int(math.sqrt(number))+1
    for i in range(2,n):
        if number%i == 0:
            return False
    return True


maxPrimes = 0
ab = [0,0]
for a in range(1000,-999,-1):
    for b in range(1001, -1000, -1):
        sumOfPrimes = 0
        n = 0
        while(isPrime(n*n+a*n+b)):
            sumOfPrimes = sumOfPrimes+1
            n=n+1
        if(sumOfPrimes > maxPrimes):
            maxPrimes = sumOfPrimes
            ab[0] = a
            ab[1] = b

print(ab)
print(ab[0] * ab[1])