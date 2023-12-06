import re
with open('input.txt','r') as f:
    time, dist = [int(re.sub(r'\s*', '', a.split(':')[1])) for a in f.read().split('\n')]
    count = 0
    for t in range(1,time):
        if t*(time-t) > dist: count += 1
    print(count)
        