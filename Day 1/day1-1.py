import os
os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 1/')

def read_file(input_file):
    text_file = open(input_file, 'r')
    data = text_file.read().rstrip().split('\n')
    text_file.close()
    return data

def func(input_file):
    data = read_file(input_file)
    data_int = [int(x) for x in data]
    answer = sum(data_int)
    return answer

func('input.txt')