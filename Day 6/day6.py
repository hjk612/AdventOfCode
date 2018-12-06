import os
import re

os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 6/')
text_file = open('input.txt', 'r')

data = text_file.read().strip()

### using regex to read the data, not required -- sort of overkill
re_pattern = re.compile('(?P<X>\d*)\, (?P<Y>\d*)')
centers = re_pattern.findall(data)

### mapping all strings to int
centers = list(map(lambda x: (int(x[0]), int(x[1])), centers))

### getting the max and min coordinates
max_x = max(centers,key=lambda item:item[0])[0]
max_y = max(centers,key=lambda item:item[1])[1]
min_x = min(centers,key=lambda item:item[0])[0]
min_y = max(centers,key=lambda item:item[1])[1]