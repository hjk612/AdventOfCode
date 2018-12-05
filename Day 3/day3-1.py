'''
Disclaimer -- could have used numpy and made things simpler by creating
a matrix. But wanted to try without using it
'''

import os
import re

os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 3/')

regex_pattern = re.compile('@\s(?P<left>\d*),(?P<top>\d*):\s(?P<dim1>\d*)x(?P<dim2>\d*)')
text_file = open('input.txt','r')
data = text_file.read()

re_results = regex_pattern.findall(data)

cloth = {}

for item in re_results:
    left = int(item[0]) + 1
    top = int(item[1]) + 1
    x = left + int(item[2]) 
    y = top + int(item[3]) 
    for i in range(left, x ):
        for j in range(top, y ):
            if (i, j) in cloth:
                cloth[(i, j)] += 1
            else:
                cloth[(i, j)] = 1
    
    