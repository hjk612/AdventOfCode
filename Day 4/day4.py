import os
import re
import datetime

os.chdir('/Users/Hatim/Desktop/Git Repos/AdventOfCode/Day 4/')

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

re_guard = re.compile('\#(\d*)\s')
                      
guard_id = None
guard_time = {}
start = None
end = None
for item in data_cleaned:
    time = item[0].minute
    status = item[1]
    if 'Guard' in status:
        guard_id = int(re_guard.findall(status)[0])
        
    elif 'asleep' in status:
        start = time
    
    elif 'wakes' in status:
        end = time
        if guard_id in guard_time:
            guard_time[guard_id].extend(list(range(start, end)))
            
        else:
            guard_time[guard_id] = list(range(start, end))
    

### getting the id of the guard who slept most
id_guard = max(guard_time, key=lambda x:len(guard_time[x]))

### getting the most common frequency
minute = max(set(guard_time[id_guard]), key=guard_time[id_guard].count)   
        
answer = id_guard * minute

### part 2

###creating a temp variable to compare the frequency of maximum frequency for each minute
max_min = -100

###the final minute answer
minute_ans = None

### the final id answer
id_ans = None
for minute in range(60):
    minute_wise = {}
    for key, value in guard_time.items():
        minute_wise[key] = value.count(minute)
    
    id_ = max(minute_wise, key=minute_wise.get)
    temp = minute_wise[id_]
    if temp > max_min:
        id_ans = id_
        minute_ans = minute
        max_min = temp
