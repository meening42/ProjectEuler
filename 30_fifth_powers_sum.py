## Problem 30
##
## As 1 = 14 is not a sum it is not included.
##
## The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##
## Find the sum of all the numbers that can be written
## as the sum of fifth powers of their digits.

import math

## check all numbers from 2 to 
string = ""
sum2 = 0
numbers = []
for i in range(4000,9999999):
    string = str(i)
    str_len = len(string)
    sum1 = 0
    for j in range(0,str_len):
        sum1 = sum1 + pow(int(string[j]),5)
    if i == sum1:
        numbers.append(i)
        sum2 = sum2 + i

print(numbers)
print(sum2)
