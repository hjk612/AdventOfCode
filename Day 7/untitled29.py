import os
import re

os.chdir('/Users/Hatim/Desktop/AdventOfCode/Day 7/')

re_pattern = re.compile('tep (?P<start>.*) m.*ep (?P<end>.*) c')