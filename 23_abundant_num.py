# -*- coding: cp1250 -*-
## problem 23
import math

def proper_div(num):
    divisor =0
    divisors = [1]
    maxn = int(math.sqrt(num))
    for i in range(2,maxn+1):
        if num%i ==0:
            divisors.append(i)
            if num/i == i:
                pass
            else:    
                divisors.append(num/i)
    return divisors

def sum_of_2_ab(num):
    ab_nums = abundant_nums(num+1)
    for i in range(0,len(ab_nums)):
        for j in range(i, len(ab_nums)):
            if ab_nums[i]+ab_nums[j] == num:
                return True
    return False

def sum_of_div(num):
    sum1 = 0
    divisors = proper_div(num)
    sum1 = sum(divisors)
    return sum1

def is_abundant(num):
    if sum_of_div(num)>num:
        return True
    else:
        return False

##def is_deficient(num):
##    if sum_of_div(num)<num:
##        return True
##    else:
##        return False
##
##def is_perfect(num):
##    if sum_of_div(num)==num:
##        return True
##    else:
##        return False
def abundant_nums(maxn):
    nums = []
    for i in range(1,maxn+1):
        if is_abundant(i):
            nums.append(i)
    return nums
##########################################
##___________MAIN PROGRAM_______________##
##########################################

maxn = 28125


## sum of all numbers to number maxn
sum1 = int((1+maxn)*(maxn/2.0))
print("Sum of all nums up to %d is %d" %(maxn,sum1))

## calculate all nums that are sum of two ab_nums
ab_nums = abundant_nums(maxn)
#print "ab_nums"
#print ab_nums
ab_len = len(ab_nums)
print("\nLength of ab nums to %d is %d" %(maxn ,len(ab_nums)))

num_2a = []
for i in range(0,ab_len):
    for j in range(i,ab_len):
        #print ab_nums[i]+ab_nums[j]
        num_2a.append(ab_nums[i]+ab_nums[j])
## Izloči podvojitve in večje od maxn
#print num_2a
print("sorting num_2a")
sorted_nums = sorted(num_2a)
#print sorted_nums
print("sorted")
num_2as =[]
numz_len = len(sorted_nums)
for k in range(0,numz_len-1):
    if sorted_nums[k] != sorted_nums[k+1]:
        #print sorted_nums[k]
        num_2as.append(sorted_nums[k])
print("num_2as")
#print num_2as
# izloči večje od 28123
m=0
num_2az = []
while num_2as[m] <= maxn:
    num_2az.append(num_2as[m])
    m=m+1
print("num_2az")
#print num_2az
print(num_2az[len(num_2az)-1])
print(num_2az[len(num_2az)-2])
print(num_2az[len(num_2az)-3])
print(num_2az[len(num_2az)-4])
#print "nums that are sums of two abs:"
#print num_2az
sum3 = 0
for l in range(0,len(num_2az)):
    sum3=sum3+num_2az[l]
print("Sum of all nums that are sum of two is %d" %sum3)

sumz = sum1 - sum3
print("sum1 " + str(sum1))
print("sum3 " + str(sum3))
print("\nSum of all nums that are not \nsums of two ab_nums until %d is =%d\n" %(maxn,sumz))



        
##for i in range(1,maxn+1):
##    posible = False ## is num sum of two abandant nums
##    for j in range(0,ab_len):
##        if ab_nums[j] > i:
##            break
##        if posible:
##            
##            break
##        for k in range(ab_len-1,-1,-1):
##            if ab_nums[j]+ab_nums[k] == i:
##                posible = True
##                print i
##                break
##    if posible == False:
##        sumz = sumz+i
            
    
