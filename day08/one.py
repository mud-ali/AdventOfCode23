with open('input.txt','r') as f:
    instructions, lines = f.read().split("\n\n")
    instructions = [1 if a=='R' else 0 for a in instructions]
    lines = lines.split("\n")
    maps = {}
    for line in lines:
        parts = line.split('=')
        maps[parts[0].strip()] = [a.strip() for a in parts[1].replace('(','').replace(')','').split(",")]

    this = "AAA"
    count = 0
    print(maps)
    while this != "ZZZ":
        dir = instructions[count % len(instructions)] 
        count += 1
        this = maps[this][dir]
    
    print(count)
        