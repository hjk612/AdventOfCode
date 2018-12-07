import os
os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 2/')

def read_file(input_file):
    text_file = open(input_file, 'r')
    data = text_file.read().rstrip().split('\n')
    text_file.close()
    return data

def match(s1, s2):
    pos = -1
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

def box_id(input_file):
    data = read_file('input.txt')
    for i in range(len(data)):
        string = data[i]
        ### the box will have many ids that are same but differ by only
        ### character at the same location
        temp_match = [match(string, s) for s in data[i+1:] if match(string, s) > -1]
        ### there will be many ids -- we only care about the common part
        if len(temp_match) > 0:
            index = temp_match[0]
            return string[:index]+string[index+1:]

answer = box_id('input.txt')
