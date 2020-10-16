import math

# prime factorisation of a number

def isPrime(number):
    n = int(math.sqrt(number))+1
    for i in range(2,n):
        if number%i == 0:
            return False
    return True    

def primeFactors(number):
    reminder = number
    primes =[]
    i =2
    while reminder>1:

        if reminder%i == 0:
           reminder = reminder/i
           primes.append(i)
           i = i-1
        i = i+1  
    return primes
   

a = primeFactors( 600851475143 )
print(a)
        
