import os
import re
import datetime

os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 4/')

text_file = open('input.txt', 'r')
data = text_file.read().rstrip()

regex_pattern = re.compile('\[(?P<datetime>.*)\]\s(?P<entry>.*)')
re_results = regex_pattern.findall(data) 

def convert_string(input_):
    '''
    function to convert string to datetime
    '''
    
    return datetime.datetime.strptime(input_, '%Y-%m-%d %H:%M')

data_cleaned = [(convert_string(x[0]), x[1]) for x in re_results]
data_cleaned.sort(key=lambda x: x[0])




