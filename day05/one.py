import re

def cleanhead(sect):
    return re.sub(r'[a-z|\-|\s]*:','',sect)

def parseMap(mapp: str) -> None:
    range_map = {}

    for line in mapp.split("\n"):
        dst, src, step = map(int, line.split())
        range_map[(src,src+step-1)] = dst-src# inclusive key value ## CONSIDER USING A SPACE DELIM STR

    return range_map

def get_data(mapy : dict, val:int) -> int:
    for start,end in mapy.keys():
        if val >= start and val <= end:
            return val + mapy[(start,end)]
    return val

with open('input.txt','r') as f:
    all_sections = [cleanhead(a)[1:] for a in f.read().split('\n\n')]
    seeds, se_soil, soi_fer, fer_water, wat_lig,\
     lig_temp, tmp_hum, hum_loc = all_sections
    seeds = list(map(int, seeds.split()))

    all_range_maps= []
    for ase in all_sections[1:]:
        all_range_maps.append(parseMap(ase))
    
    smallest_location = 999999999999
    for seed in seeds:
        vall = seed
        for ranger in all_range_maps:
            vall = get_data(ranger, vall)
        if vall < smallest_location: smallest_location = vall
    
    print(smallest_location)


    