import os
os.chdir('/Users/Hatim/Desktop/Git Repos/AdventOfCode/Day 5/')

text_file = open('input.txt', 'r')
string = text_file.read().rstrip()

def explosion(string, i):
    return string[:i] + string[i+2:]

def reaction(string):
    length = len(string)
    index = 0
    while index < (length - 1):
        if index < 0:
            index = 0
        first = string[index]
        second = string[index+1]
        if first.lower() == second.lower() and first != second:
            string = explosion(string, index)
            length -= 2
            index -= 2
        
        index += 1

    return length

part1 = reaction(string) 


part2 = 10000000000000
alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
for alphabet in alphabets:
    swaps = {alphabet: '', alphabet.upper(): ''}
    string_temp = ''.join(swaps.get(i,i) for i in string)
    string_reaction = reaction(string_temp)
    part2 = min(part2, string_reaction)