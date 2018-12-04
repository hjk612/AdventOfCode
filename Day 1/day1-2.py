import os
os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 1/')

def read_file(input_file):
    text_file = open(input_file, 'r')
    data = text_file.read().rstrip().split('\n')
    text_file.close()
    return data

def func(input_file):
    data = read_file(input_file)
    data = [int(x) for x in data]
    dict_ = set()
    dict_.add(0)
    sum_ = 0
    flag = True
    while flag:
        for i in data:
            sum_ += i
            if sum_ in dict_:
                flag = False
                break
            dict_.add(sum_)
    return sum_
            