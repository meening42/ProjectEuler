##problem 10
##
##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.

import math

def isPrime(number):
    n = int(math.sqrt(number))+1
    for i in range(2,n):
        if number%i == 0:
            return False
    return True

primes = [2] # make a list of primes (starting with first prime)

for i in range(3,2000000,2):
    if isPrime(i):
        primes.append(i)

#print primes
print(sum(primes))
