##  problem 24
## 
##  What is the millionth lexicographic permutation of the
##  digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import math

def switch(d1,d2,list1):
    temp = list1[d2]
    list1[d2]=list1[d1]
    list1[d1]=temp
    return list1


###########################################
##_______________Main Program___________###
###########################################

num_of_dig = 10
nthp = 1000000 # n-th permutation
digits = []
## num of permutations
num_of_permutations = math.factorial(num_of_dig)
print("number of all permutations is: %d" %num_of_permutations)

## FIRST PERMUTATION
nthp = nthp - 1  ## we start from zero 
per1 = []
for i in range(0,num_of_dig):
    per1.append(i)
print(per1)

## temp_val must become the same as nthp
new_set_of_num = per1
temp_val     = 0
magnitude    =  num_of_permutations 
nth_permutation = []
temp_val=0

print("\nNTHP = " +str(nthp) )
for j in range(0,num_of_dig): ## ugotovimo stevilko na vsakem mestu
    magnitude = magnitude / (num_of_dig-j)
    k=0
    #print "magnitude" + str(magnitude)
    while temp_val < nthp:
        print("j= " +str(j)+ "   "+"temp_val= "+str(temp_val))
        if temp_val == nthp:
            print("we found your permutation ")
        temp_val = temp_val+magnitude
        k=k+1
    if temp_val != nthp:
        temp_val = temp_val - magnitude
        k = k-1 
    nth_permutation.append(new_set_of_num[k])
    print("nth_permutation = " +str(nth_permutation))
    
    new_set_of_num.remove(new_set_of_num[k])        
    print("new set of num = " + str(new_set_of_num))

print("You are searching for %d th premutation " %nthp)
print(nth_permutation)
for c in nth_permutation:
    print(c,end='')
     
 


