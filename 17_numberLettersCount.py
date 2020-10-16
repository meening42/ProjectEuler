# problem 17

def num2letterNum(num):
    num2let = {0: '',
                   1: "one",
                   2: "two",
                   3: "three",
                   4: "four",
                   5: "five",
                   6: "six",
                   7: "seven",
                   8: "eight",
                   9: "nine",
                   10: "ten",   ## ten21121
                   11: "eleven",
                   12: "twelve",
                   13: "thirteen",
                   14: "fourteen",
                   15: "fifteen",
                   16: "sixteen",
                   17: "seventeen",
                   18: "eighteen",
                   19: "nineteen",
                   20: "twenty", ## over tventy
                   30: "thirty",
                   40: "forty",
                   50: "fifty",
                   60: "sixty",
                   70: "seventy",
                   80: "eighty",
                   90: "ninety",
                   100: "onehundred", ## hundred
                   1000: "onethousand"}
    if num ==100:
        return num2let[100]
    if num == 1000:
        return num2let[1000]
    if num%100==0 and num>100:
        hundreds = int(num/100)
        return num2let[hundreds]+"hundred"
    if num >=100:
        ones = num %10
        hundreds = int(num/100)
        tens = int((num-hundreds*100)/10)
        if tens == 1:
            return num2let[hundreds] + "hundredand" + num2let[num%100]
        return num2let[hundreds] + "hundredand" + num2let[tens*10] + num2let[ones]
    if num >=  0 and num <100:
        ones = num%10
        tens = int(num/10)
        if num<20:
            return num2let[num]
        return num2let[tens*10] + num2let[ones]

sum1 = 0
for i in range(1,1001):
    sum1 = sum1 + len(num2letterNum(i))
    print(str(i)+ ' ' +num2letterNum(i) +'  .... '+ str(len(num2letterNum(i)))+'___' +str(sum1)   )
print('the sum of all numbers from 1 to 100 eaqals = ' + str(sum1))


