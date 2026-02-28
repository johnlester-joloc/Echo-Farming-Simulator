from Models.EchoBase import EchoBase
from random import random

def buildOneCostEcho(name: str, set : str):
    main_stats = {
        "ATK%": 3.6,
        "HP%": 4.5,
        "DEF%": 3.6,
        
    }
    main_stat = random.choice(list(main_stats.keys()))
    flat_hp = 456
    return EchoBase(name, set, 1, main_stat, main_stats[main_stat], "HP", flat_hp, [])
