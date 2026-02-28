from Models.EchoBase import EchoBase
from random import random

def buildOneCostEcho(name: str, set : str):
    main_stats = {
        "ATK%": 3.6,
        "HP%": 4.5,
        "DEF%": 3.6,
        
    }
    flat_hp = 456
    return EchoBase(name, set, 1, 
                    random.choice(list(main_stats.keys())), 
                    main_stats[random.choice(list(main_stats.keys()))], 
                    "HP", flat_hp, [])