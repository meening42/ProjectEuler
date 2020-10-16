## Problem 18

t1 = [[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3]]

t2 = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

t3 = """03
07 04
02 04 06
08 05 09 03 """

t4 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 """

import math

def getNumFromTriangle(row,index,triangle):
    a= index*3
    firstNum=0
    for b in range(0,row+1):
        firstNum = firstNum+b
    firstNum = firstNum*3+a
    
    number = int(triangle[firstNum]+triangle[firstNum+1])
    return number

def triangleSize(triangle):
    numOfNum = len(triangle)/3  #number of numbers in triangle
    #print numOfNum
    numOfRow =0
    i=1
    j=1
    while i<=numOfNum:
        j=j+1
        i=i+j
        numOfRow=numOfRow+1
    return numOfRow-1

## main program

myTriangle = t4

        
numOfRow = triangleSize(myTriangle)
numOfPaths = int (math.pow(2,numOfRow))-1
maxsum = 0
rightPath = ''

for i in range(0,numOfPaths+1):
    sum1=getNumFromTriangle(0,0,myTriangle)   # zgornja stevilka
    d = bin(i)
    d=d[2:]
    while len(d) < numOfRow:
        d='0'+d
    strl = len(d)
    #print ('new path is = '+d)
    c=0
    for j in range(0,strl):
        r=1
        if d[j]=='1':
            c=c+1
            sum1 = sum1 + getNumFromTriangle(j+1,c,myTriangle)
            #print getNumFromTriangle(r,c,myTriangle)
            #print ('j+1 = '+str(j+1)+'    c= '+str(c))
        if d[j]=='0':
            sum1 = sum1 + getNumFromTriangle(j+1,c,myTriangle)
            #print getNumFromTriangle(j+1,c,myTriangle)
            #print ('j+1 = '+str(j+1)+'    c= '+str(c))
    if sum1 > maxsum:
        maxsum = sum1
        rightPath = d
        
print('maximum sum is: ' +str(maxsum))
#print('Right path is '+ str(rightPath))

#print(getNumFromTriangle(3,1,myTriangle))

    
        























