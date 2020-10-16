# problem 20

num = 100
factorial = 1
for i in range(1,num+1):
    factorial=factorial*i


print("The number is: " + str(factorial))

l = len(str(factorial))

print("Number of digits is: "+str(l))

factorial_s = str(factorial) # int to string
sum = 0
for j in range(0,l):
    sum = sum + int(factorial_s[j])

print("Sum of digits is: "+str(sum))
