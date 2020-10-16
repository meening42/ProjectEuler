##  problem 24
## What is the index of the first term in the Fibonacci
## sequence to contain 1000 digits?

## f1 = 1
## f2 = 1
## f3 = 2
## f4 = 3
## f5 = 5

fn1 = 1
fn = 1
dig_len = len(str(fn))
num_of_dig = 1000
num_of_dig = num_of_dig-1
i = 2
while dig_len<=num_of_dig:
    dig_len = len(str(fn))
    temp = fn
    fn = fn+fn1
    fn1 = temp
    
    #print str(i) + "  fn1 = " + str(fn1) + "    dig_len = " + str(dig_len)
    i=i+1
    #print "fn = " + str(fn) + "\n"
    
print(str(i-1) + "  fn1 = " + str(fn1) + "    dig_len = " + str(dig_len))
