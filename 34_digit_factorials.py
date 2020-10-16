# -*- coding: utf-8 -*-
## problem 34

import math

## check all numbers from 2 to 
string = ""
sum2 = 0
numbers = []
for i in range(3,9999999):
    string = str(i)
    str_len = len(string)
    sum1 = 0
    for j in range(0,str_len):
        sum1 = sum1 + math.factorial(int(string[j]))
    if i == sum1:
        numbers.append(i)
        sum2 = sum2 + i

print(numbers)
print(sum2)
