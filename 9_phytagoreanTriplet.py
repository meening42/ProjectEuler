# proble  9
##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
##a2 + b2 = c2
##For example, 32 + 42 = 9 + 16 = 25 = 52.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

# generate a,b,c so that a+b+c = 1000
# check if a2+b2=c2
# include law a<b<c

# generate a
for a in range(1,333):
    # calculate max b and c
    temp1 = 1000-a
    maxb = int(temp1/2)
    for b in range(a+1,maxb):
        c = 1000 - (a+b)
        if a*a + b*b == c*c:
            print ('a = '+str(a)+' b = '+str(b)+' c = '+str(c))
            print((a*b*c))
    
    
