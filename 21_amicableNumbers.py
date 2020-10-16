# problem 21
import math

def divisors(num):
    div =[]
    for i in range(1,int(num/2)+1):
        if num%i ==0:
            div.append(i)
    return div


def sumOfArray(array):
    a=len(array)
    sumArray=0
    for i in range(0,a):
        sumArray=sumArray + array[i]
    return sumArray

amicables = []

for i in range(1,10001):
    if  sumOfArray(divisors(sumOfArray(divisors(i)))) == i and i!=sumOfArray(divisors(i)):
        amicables.append(i)

print(amicables)
print(sumOfArray(amicables))
