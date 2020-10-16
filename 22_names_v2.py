# Problem 22

# USE WindowsPowerShell go to path of this file
# and type python 22_names_v2.py p022_names.txt

def sort_names(string1):
    # find names and put them in list
    index1 = 0
    i = 1
    names = []
    while i < len(string1):
        index1 = 0
        name  = ''
        while  string1[i] != '"':
            name = name +  string1[i]
            i=i+1
            index1 = index1 + 1
        names.append(name)
        i = i+3
    return sorted(names),

## IMPORT LIBRARIES
from sys import argv
import sys
from os.path import exists

# MAIN PROGRAM
script , file_name = argv
if exists(file_name):
    myfile = open(file_name,'r')
    str1 = myfile.read()
    myfile.close()
else:
    sys.exit("\nThere is no such file.\nPlease check the path name.  :D\n")

## SORT NAMES
names_srtd = sort_names(str1)
#print str1
#print names_srtd
print('\n')


## SCORE NEMES
score = 0
scores = []
for i in range(0,len(names_srtd[0])):
    score = 0
    name = names_srtd[0][i]
    print(names_srtd[0][i])
    for j in range (0,len(name)):
        score = score + ord(name[j])-64
        print(name[j] + ' ' + str(ord(name[j])-64))
    scores.append(score)
    #print scores

full_score = 0
score2 = 0
print(len(scores))
for k in range(0,len(scores)):
    score2 = (k+1) * scores[k]
    #print str(k+1) + ' * '+ str(scores[k])+ ' = ' + str(score2)
    full_score = full_score + score2
print(full_score)





