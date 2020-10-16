def multiplesOf(number,maxnum):
    a = list(range(1,int(maxnum/number)+1))
    for i in a:
        a[i-1]=a[i-1]*number
    return a

def multiplesOfBoth(num1,num2,maxnum):
    a = list(range(1,int(maxnum/(num1*num2))+1))
    for i in a:
        a[i-1]=a[i-1]*num1*num2
    return a
    

maxi = 999
a = multiplesOf(3,maxi)
b = multiplesOf(5,maxi)
c = multiplesOfBoth(3,5,maxi)

result = sum(a)+sum(b)-sum(c)
print(result)

   
