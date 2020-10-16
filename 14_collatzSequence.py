# -*- coding: utf-8 -*-
#problem 14
##The following iterative sequence is defined for the set of positive integers:
##
##n → n/2 (n is even)
##n → 3n + 1 (n is odd)
##
##Using the rule above and starting with 13, we generate the following sequence:
##
##13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##
##Which starting number, under one million, produces the longest chain?

def collatzSeq(num):
    seq = [num]
    i = 0
    while seq[i]!=1:
        if seq[i]%2==0:
            temp=seq[i]/2
            seq.append(temp)
        else:
            temp = seq[i]*3+1
            seq.append(temp)
        i=i+1
    return seq

def invCollatzNum(num):
    i =1
    return i

## Main program
maxNum = 1
length = 1
for j in range(2,1000000):
    if len(collatzSeq(j))>length:
        length = len(collatzSeq(j))
        maxNum = j

print(len(collatzSeq(maxNum)))
print(maxNum)
print(collatzSeq(maxNum))
