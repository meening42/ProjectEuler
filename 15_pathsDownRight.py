# problem 15

import math 
side_a = 20
side_b = 20

posib = side_a + side_b

def factorial(num):
    a = 1
    for i in range(1,num+1):
        a = a*i
    return a

## program :

p = factorial(posib) / (factorial(side_a)*factorial(side_a))


print(p)
