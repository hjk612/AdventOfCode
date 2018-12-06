'''
Disclaimer -- Not an optimal solution.
Takes quite some time. Will try to improve it over the next few days
'''

import os
os.chdir('/Users/Hatim/Desktop/Git Repos/AdventOfCode/Day 5/')

text_file = open('input.txt', 'r')
string = text_file.read().rstrip()

def explosion(string, i):
    return string[:i] + string[i+2:]

should_restart = True
while should_restart:
    should_restart = False
    for i in range(len(string)-1):
        first = string[i]
        second = string[i+1]
            
        if first.lower() == second.lower() and first != second:
            string = explosion(string, i)
            should_restart = True
            break

answer = len(string)