'''
Disclaimer -- could have used numpy and made things simpler by creating
a matrix. But wanted to try without using it
'''

import os
import re

os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 3/')

### used pythex -- https://pythex.org
regex_pattern = re.compile('#(?P<id>\d*)\s@\s(?P<left>\d*),(?P<top>\d*):\s(?P<dim1>\d*)x(?P<dim2>\d*)')
text_file = open('input.txt','r')
data = text_file.read()

re_results = regex_pattern.findall(data)

cloth = {}
for item in re_results:
    id_ = int(item[0])
    left = int(item[1]) + 1
    top = int(item[2]) + 1
    x = left + int(item[3]) 
    y = top + int(item[4]) 
    for i in range(left, x):
        for j in range(top, y):
            if (i, j) in cloth:
                cloth[(i, j)] += 1
            else:
                cloth[(i, j)] = 1


for item in re_results:
    id_ = int(item[0])
    left = int(item[1]) + 1
    top = int(item[2]) + 1
    x = left + int(item[3]) 
    y = top + int(item[4])
    flag = True
    for i in range(left, x):
        for j in range(top, y):
            if cloth[(i,j)] > 1:
                flag = False
                continue
        
        if flag == False:
            continue
    if flag == True:
        answer = id_
    
            

    