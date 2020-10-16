def fiboToNum(maxnum):
    fib_list=[1,2]
    i = 1
    while (fib_list[i]+fib_list[i-1])<maxnum:
        temp = fib_list[i]+fib_list[i-1]
        temp2 = [temp]
        fib_list = fib_list+temp2
        i=i+1
    return fib_list

# fibonachi sequence
a=fiboToNum(4000000)
print(a)

sum = 0
for fib in a:
    if(fib%2==0):
        sum = sum + fib


print(sum)


 
