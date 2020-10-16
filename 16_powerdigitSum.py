# problem 16

power=1
for i in range(0,1000):
    power=power*2


print("The number is: " + str(power))

l = len(str(power))

print("Number of digits is: "+str(l))

power_s = str(power) # int to string
sum = 0
for j in range(0,l):
    sum = sum + int(power_s[j])

print("Sum of digits is: "+str(sum))
