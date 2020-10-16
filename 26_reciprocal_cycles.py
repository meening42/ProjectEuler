##  problem 26

##  Find the value of d < 1000 for which 1/d contains the
##  longest recurring cycle in its decimal fraction part.



def oneDivBy(num,max_decimal_places):
    string = "0."
    if num <= 1:
        return 0
    dividend = 1
    temp_dividend = dividend
    decimal_place = 0
    remainder = 0

    while decimal_place < max_decimal_places:
        if num > temp_dividend:
            temp_dividend = temp_dividend*10
            decimal_place = decimal_place + 1
        digit     = temp_dividend / num
        remainder = temp_dividend % num
        string = string + str(digit)
        temp_dividend = remainder 
        if remainder == 0:
            break
    return string

def recurring_length(num, max_decimal_places):
    string = oneDivBy(num,max_decimal_places)
    ## cut of the 0. from the string
    string = string[2:]
    if len(string) < max_decimal_places:
        ## then no reacuring
        return 0, string 
    start_digit = len(str(num))+1
    length = 0
    cycle_not_found = True
    while cycle_not_found:
        if length > len(string):
            return -1, string
        length = length +1
        temp_string = string[start_digit:start_digit+length]
        if temp_string == string[start_digit+length:start_digit+2*length]:
            if length < 3:
                if temp_string == string[start_digit+2*length:start_digit+3*length]:
                    cycle_not_found = False
            if length >= 3:
                cycle_not_found = False
            
    return length, string
temp_index =0
largest  =0
for i in range(2,1000):
    temp =recurring_length(i,2000)
    #print " \n 1/" + str(i) + "     "  + str(temp)
    if largest < temp[0]:
        largest = temp[0]
        temp_index = i

print(largest )
print(temp_index)
