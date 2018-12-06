import os
import re
import numpy as np
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
min_y = min(centers,key=lambda item:item[1])[1]

counter = [0]*len(centers)

def manhattan_distance(p, q):

    if(len(p) != len(q)):
       print("Be sure that both vectors are the same dimension!")
       return

    return sum([abs(p[i] - q[i]) for i in range(len(p))])

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distance = np.array([manhattan_distance((x,y), c) for c in centers])
        num_closest_center = np.sum(distance == distance.min())
        if num_closest_center > 1:
            continue
        if not (x == min_x or x == min_x or x == max_x or y == min_y or y == max_y):
            counter[np.argmin(distance)] += 1
        else:
            counter[np.argmin(distance)] += 1e10
    
counter = np.array(counter, dtype = int)
part1 = counter[counter<1e10].max()
        