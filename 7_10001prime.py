# Problem 7 _____10001 prime number
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?
import math

def isPrime(number):
    n = int(math.sqrt(number))+1
    for i in range(2,n):
        if number%i == 0:
            return False
    return True

number = 2
prime = 1
while prime <= 10001:
    if isPrime(number):
        #print('prime '+str(prime)+' is number '+str(number))
        prime=prime+1    
    number = number +1   
    
print(number-1)
      


