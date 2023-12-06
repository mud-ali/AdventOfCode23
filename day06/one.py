with open('input.txt','r') as f:
    times, dists = [list(map(int, a.split(":")[1].strip().split())) for a in f.read().split('\n')]
    mult = 1
    for idx, time in enumerate(times):
        count = 0
        print(f'time={time}')
        for i in range(time+1):
            dist = i * (time-i)
            if dist > dists[idx]:
                count += 1
            print(i,dist, dist > dists[idx])
        mult *= count
    print(mult)

            