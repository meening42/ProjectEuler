# -*- coding: utf-8 -*-
# problem 6
##The sum of the squares of the first ten natural numbers is,
##
##1on2 + 2on2 + ... + 10on2 = 385
##The square of the sum of the first ten natural numbers is,
##
##(1 + 2 + ... + 10)on2 = 55on32 = 3025
##Hence the difference between the sum of the squares of the first
##ten natural numbers and the square of the sum is 3025 − 385 = 2640.
##
##Find the difference between the sum of the squares of the first
##one hundred natural numbers and the square of the sum.


# sum of squares

def sumOfSquares(num):
    sum1 = 0
    for i in range(1,int(num)+1):
        sum1= sum1 + i*i
    return sum1

def squareOfSum(num):
    sum1 = 0
    for i in range(1,int(num)+1):
        sum1 = sum1+i
    sum1 = sum1*sum1
    return sum1

    
print('To what number should I go')
number = input()
print('Sum of squares')
a = sumOfSquares(number)
print(a)
print ('Square of sums')
b = squareOfSum(number)
print(b)

print('diference between numbers is:  ')
difer = b-a
print(difer)
