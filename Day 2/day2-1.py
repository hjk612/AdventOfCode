import os
os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 2/')

def read_file(input_file):
    text_file = open(input_file, 'r')
    data = text_file.read().rstrip().split('\n')
    text_file.close()
    return data

def char_frequency(str1):
    dict_ = {}
    for n in str1:
        keys = dict_.keys()
        if n in keys:
            dict_[n] += 1
        else:
            dict_[n] = 1
    return dict_

def func(input_file):
    data = read_file(input_file)
    two = 0
    three = 0
    for string in data:
        char_dict = char_frequency(string)
        vals = char_dict.values()
        if 2 in vals:
            two += 1
        if 3 in vals:
            three += 1
        
    return two*three 

func('input.txt')