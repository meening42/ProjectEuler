
def isPalindrome(a):
    if str(a) == str(a)[::-1]:
        return True
    return False

found = False
palindromeList = []

for i in range(1000,99,-1):
    for j in range(1000,99,-1):
        if(isPalindrome(i*j)):
            palindromeList.append(i*j)


print(max(palindromeList))
print("End")