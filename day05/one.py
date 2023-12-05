import re

def cleanhead(sect):
    return re.sub(r'[a-z|\-|\s]*:','',sect).strip()

def parseMap(map: str, name:str) -> None:
    pass

with open('input.txt','r') as f:
    all_sections = [cleanhead(a) for a in f.read().split('\n\n')]
    seeds, se_soil, soi_fer, fer_water, wat_lig,\
     lig_temp, tmp_hum, hum_loc = all_sections
    seeds = list(map(int, seeds.split()))
    for seed in seeds:
        pass

    