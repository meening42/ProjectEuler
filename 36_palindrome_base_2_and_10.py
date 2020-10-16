## problem 36

## The decimal number, 585 = 1001001001
## (binary), is palindromic in both bases.
##
## Find the sum of all numbers, less than one
## million, which are palindromic in base 10 and base 2.
##
## (Please note that the palindromic number, in
##  either base, may not include leading zeros.)

sum1 = 0
for i in range(0,1000000):
    # binary
    i_b = str(bin(i))
    i_b = i_b[2:]

    # reversed string
    rev_i = str(i)[::-1]
    rev_i_b = str(i_b)[::-1]

    if (rev_i == str(i)) and (rev_i_b==str(i_b)):
        sum1=sum1+i

print(sum1)

    
    
    


